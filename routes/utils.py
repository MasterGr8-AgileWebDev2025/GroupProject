"""
Utility functions for routes
"""
from datetime import datetime
from flask import abort
from flask_login import current_user
from models import Match, SharedAnalysis

def check_match_access(match_id):
    """
    Check if the current user has access to the specified match.
    Returns the match object if access is granted, otherwise aborts with 403.
    """
    match = Match.query.get_or_404(match_id)
    
    # Check if the user owns the match
    if match.user_id == current_user.id:
        return match
        
    # Check if the match is shared with the user
    shared = SharedAnalysis.query.filter_by(
        match_id=match.id, 
        shared_with_id=current_user.id
    ).first()
    
    if shared:
        return match
    
    # User does not have access
    abort(403)

def get_template_date():
    """Helper to get the current datetime for templates"""
    return {'now': datetime.utcnow()}