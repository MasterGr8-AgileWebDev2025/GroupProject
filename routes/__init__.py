"""
Tennis Analytics Platform Routes Package
"""
from flask import Flask

def register_blueprints(app):
    """
    This function registers all the blueprints with the Flask application.
    It imports the blueprints from their respective modules and then registers them.
    """
    # Importing blueprints from their respective modules
    from routes.main_routes import main_bp
    from routes.auth_routes import auth_bp
    from routes.user_routes import user_bp
    from routes.match_routes import match_bp
    from routes.api_routes import api_bp
    from routes.share_routes import share_bp
    
    # Registering the blueprints with the Flask application
    app.register_blueprint(main_bp)  # Registers the main routes blueprint
    app.register_blueprint(auth_bp)  # Registers the authentication routes blueprint
    app.register_blueprint(user_bp)  # Registers the user routes blueprint
    app.register_blueprint(match_bp)  # Registers the match routes blueprint
    app.register_blueprint(api_bp)  # Registers the API routes blueprint
    app.register_blueprint(share_bp)  # Registers the share routes blueprint