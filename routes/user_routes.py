"""
User-related routes for Tennis Analytics Platform
"""
from datetime import datetime
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from models import User, Match, MatchStatistic, SharedAnalysis
from forms import ProfileUpdateForm
from helpers import get_user_statistics
from routes.utils import get_template_date

# Create blueprint
user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard route"""
    # Get user's match history
    matches = Match.query.filter_by(user_id=current_user.id).order_by(Match.date.desc()).limit(5).all()
    
    # Get matches shared with the user
    shared_matches_query = SharedAnalysis.query.filter_by(shared_with_id=current_user.id).join(
        Match, Match.id == SharedAnalysis.match_id
    ).order_by(Match.date.desc())
    
    shared_matches = []
    for share in shared_matches_query.limit(5).all():
        shared_matches.append({
            'match': share.match,
            'shared_by': User.query.get(share.shared_by_id)
        })
    
    # Get user statistics
    stats = get_user_statistics(current_user.id)
    
    return render_template(
        'dashboard.html',
        matches=matches,
        shared_matches=shared_matches,
        stats=stats,
        **get_template_date()
    )

@user_bp.route('/history')
@login_required
def history():
    """User match history route"""
    matches = Match.query.filter_by(user_id=current_user.id).order_by(Match.date.desc()).all()
    
    # Get matches shared with the user
    shared_matches_query = SharedAnalysis.query.filter_by(shared_with_id=current_user.id).join(
        Match, Match.id == SharedAnalysis.match_id
    ).order_by(Match.date.desc())
    
    shared_matches = []
    for share in shared_matches_query.all():
        shared_matches.append({
            'match': share.match,
            'shared_by': User.query.get(share.shared_by_id)
        })
    
    return render_template(
        'history.html',
        user_matches=matches,
        shared_matches=shared_matches,
        **get_template_date()
    )

@user_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """User profile route"""
    form = ProfileUpdateForm()
    
    if form.validate_on_submit():
        # Verify current password
        if not current_user.check_password(form.current_password.data):
            flash('Current password is incorrect.', 'danger')
            return render_template('profile.html', form=form, **get_template_date())
        
        # Check if username is taken by someone else
        if form.username.data != current_user.username:
            existing_user = User.query.filter_by(username=form.username.data).first()
            if existing_user:
                flash('Username already taken. Please choose another.', 'danger')
                return render_template('profile.html', form=form, **get_template_date())
        
        # Check if email is taken by someone else
        if form.email.data != current_user.email:
            existing_user = User.query.filter_by(email=form.email.data).first()
            if existing_user:
                flash('Email already registered. Please use another.', 'danger')
                return render_template('profile.html', form=form, **get_template_date())
        
        # Update user info
        current_user.username = form.username.data
        current_user.email = form.email.data
        
        # Update password if provided
        if form.new_password.data:
            current_user.set_password(form.new_password.data)
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('user.profile'))
    
    # Pre-populate form fields
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    # Get some stats
    match_count = Match.query.filter_by(user_id=current_user.id).count()
    shared_with_me = SharedAnalysis.query.filter_by(shared_with_id=current_user.id).count()
    shared_by_me = SharedAnalysis.query.filter_by(shared_by_id=current_user.id).count()
    
    stats = {
        'account_age': (datetime.utcnow() - current_user.created_at).days,
        'match_count': match_count,
        'shared_with_me': shared_with_me,
        'shared_by_me': shared_by_me
    }
    
    return render_template('profile.html', form=form, stats=stats, **get_template_date())