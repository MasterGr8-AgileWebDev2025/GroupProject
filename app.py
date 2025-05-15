import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_migrate import Migrate

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Set up database
class Base(DeclarativeBase):
    pass

class Config:
    SECRET_KEY = os.environ.get("SESSION_SECRET", "tennis-analytics-secret-key")

class DeploymentConfig(Config):
    db_uri = "sqlite:///tennis_analytics.db"

class TestingConfig(Config):
    db_uri = 'sqlite:///:memory'



db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()


# Create the app
def create_application(Config):
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    # Configure the database with SQLite
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.db_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # from routes.main_routes import main_bp
    # app.register_blueprint(main_bp)

    # Initialize the app with the extension
    db.init_app(app)
    migrate = Migrate(app, db)

    # Initialize login manager

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Import models after db initialization to avoid circular imports
    with app.app_context():
        from models import User, Match, MatchStatistic, SharedAnalysis
    
        db.create_all()
    
        # Setup user loader
        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))
    
        # Import and register blueprint routes
        from routes import register_blueprints
        register_blueprints(app)

    return app


app = create_application(DeploymentConfig)