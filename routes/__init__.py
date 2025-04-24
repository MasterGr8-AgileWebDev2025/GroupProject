"""
Tennis Analytics Platform Routes Package
"""
from flask import Flask

def register_blueprints(app):
    """Register all blueprints with the Flask application"""
    from routes.main_routes import main_bp
    from routes.auth_routes import auth_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)