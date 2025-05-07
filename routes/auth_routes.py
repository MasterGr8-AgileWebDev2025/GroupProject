"""
Authentication routes for Tennis Analytics Platform
"""
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from models import User
from forms import LoginForm, RegistrationForm
from routes.utils import get_template_date

# Create blueprint
auth_bp = Blueprint('auth', __name__)

# TODO: should we add basic response check as unit test here?
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    form = RegistrationForm()
    
    if form.validate_on_submit():
        # Check if username or email already exists
        existing_user = User.query.filter(
            (User.username == form.username.data) | 
            (User.email == form.email.data)
        ).first()
        
        if existing_user:
            if existing_user.username == form.username.data:
                flash('Username already taken. Please choose another.', 'danger')
            else:
                flash('Email already registered. Please use another or login.', 'danger')
            return render_template('register.html', form=form, **get_template_date())
        
        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        
        # Add to database
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! You can now login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html', form=form, **get_template_date())

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login route"""
    if current_user.is_authenticated:
        return redirect(url_for('user.dashboard'))
        
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('Login successful!', 'success')
            return redirect(next_page or url_for('user.dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
    
    return render_template('login.html', form=form, **get_template_date())

@auth_bp.route('/logout')
def logout():
    """User logout route"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))