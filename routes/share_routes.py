"""
Sharing routes for Tennis Analytics Platform
"""
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from app import db
from models import User, Match, SharedAnalysis
from forms import MatchShareForm
from routes.utils import check_match_access, get_template_date

# Create blueprint
share_bp = Blueprint('share', __name__)

@share_bp.route('/share', methods=['GET', 'POST'])
@login_required
def share():
    """Match sharing route"""
    form = MatchShareForm()
    
    # Get matches the user can share
    matches = Match.query.filter_by(user_id=current_user.id).order_by(Match.date.desc()).all()
    
    # Process share form
    if form.validate_on_submit():
        # Check if match exists and belongs to current user
        match = Match.query.get_or_404(form.match_id.data)
        if match.user_id != current_user.id:
            flash('You can only share your own matches.', 'danger')
            return redirect(url_for('share.share'))
        
        # Check if user exists
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash(f'User {form.username.data} not found.', 'danger')
            return render_template('share.html', form=form, matches=matches, **get_template_date())
        
        # Don't share with self
        if user.id == current_user.id:
            flash('You cannot share a match with yourself.', 'danger')
            return render_template('share.html', form=form, matches=matches, **get_template_date())
        
        # Check if already shared
        existing_share = SharedAnalysis.query.filter_by(
            match_id=match.id,
            shared_by_id=current_user.id,
            shared_with_id=user.id
        ).first()
        
        if existing_share:
            flash(f'Match already shared with {user.username}.', 'info')
            return redirect(url_for('share.share'))
        
        # Create new share
        share = SharedAnalysis(
            match_id=match.id,
            shared_by_id=current_user.id,
            shared_with_id=user.id
        )
        
        db.session.add(share)
        db.session.commit()
        
        flash(f'Match shared successfully with {user.username}!', 'success')
        return redirect(url_for('share.share'))
    
    # Get the users I've shared with
    shares = SharedAnalysis.query.filter_by(shared_by_id=current_user.id).all()
    
    shared_with = {}
    for share in shares:
        if share.match_id not in shared_with:
            shared_with[share.match_id] = []
        
        shared_with[share.match_id].append(User.query.get(share.shared_with_id).username)
    
    return render_template(
        'share.html',
        form=form,
        matches=matches,
        shared_with=shared_with,
        **get_template_date()
    )