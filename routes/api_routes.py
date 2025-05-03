"""
API routes for Tennis Analytics Platform
"""
from flask import Blueprint, jsonify, abort
from flask_login import current_user, login_required
from models import Match, SharedAnalysis

# Create blueprint
api_bp = Blueprint('api', __name__)

@api_bp.route('/api/match/<int:match_id>/statistics')
@login_required
def get_match_statistics(match_id):
    """API endpoint to get match statistics"""
    match = Match.query.get_or_404(match_id)
    
    # Check if user has access to this match
    if match.user_id != current_user.id:
        shared = SharedAnalysis.query.filter_by(
            match_id=match.id, 
            shared_with_id=current_user.id
        ).first()
        
        if not shared:
            abort(403)
    
    statistics = match.statistics.all()
    
    # Organize statistics for JSON response
    response = {}
    for stat in statistics:
        response[stat.statistic_type] = stat.get_data()
    
    return jsonify(response)