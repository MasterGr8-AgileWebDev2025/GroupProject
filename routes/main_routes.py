"""
Main routes for Tennis Analytics Platform
"""
from flask import Blueprint, render_template, send_file
from flask_login import current_user
import os
from routes.utils import get_template_date

# Create blueprint
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Homepage route: Renders the index.html template with the current datetime."""
    return render_template('index.html', **get_template_date())

@main_bp.route('/about')
def about():
    """About page route: Renders the about.html template with the current datetime."""
    return render_template('about.html', **get_template_date())

@main_bp.route('/download/template')
def download_excel_template():
    """Download Excel template route: Sends the tennis_match_template.xlsx file for download."""
    # Construct the path to the Excel template file
    template_path = os.path.join(os.getcwd(), 'static', 'templates', 'tennis_match_template.xlsx')
    # Send the file for download with the specified name and as an attachment
    return send_file(template_path, 
                     download_name='tennis_match_template.xlsx',
                     as_attachment=True)