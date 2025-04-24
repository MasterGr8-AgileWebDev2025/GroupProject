"""
Legacy routes file for backward compatibility.
This file is only here for transitional purposes.
All routes have been moved to the routes/ package.
"""

# Make the import work in old code that might still use routes.xxx
from routes.main_routes import *
from routes.auth_routes import *

# For migration purposes
def register_with_app(app):
    """
    Legacy function for backward compatibility.
    This will be removed in the future.
    """
    from routes import register_blueprints
    register_blueprints(app)