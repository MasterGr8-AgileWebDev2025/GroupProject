from routes.main_routes import *
from routes.match_routes import *

def register_with_app(app):
    """
    Legacy function for backward compatibility.
    This will be removed in the future.
    """
    from routes import register_blueprints
    register_blueprints(app)