"""
Main routes for Tennis Analytics Platform
"""
from flask import Blueprint, render_template, send_file
from flask_login import current_user
import os
from routes.utils import get_template_date

# Create blueprint
main_bp = Blueprint('main', __name__)

# TODO: should we add unit test here?
@main_bp.route('/')
def index():
    """Homepage route"""
    return render_template('index.html', **get_template_date())

@main_bp.route('/about')
def about():
    """About page route"""
    return render_template('about.html', **get_template_date())

@main_bp.route('/download/template')
def download_excel_template():
    """Download Excel template route"""
    template_path = os.path.join(os.getcwd(), 'static', 'templates', 'tennis_match_template.xlsx')
    return send_file(template_path, 
                     download_name='tennis_match_template.xlsx',
                     as_attachment=True)