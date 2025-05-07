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

db = SQLAlchemy(model_class=Base)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "tennis-analytics-secret-key")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure the database with SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tennis_analytics.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the app with the extension
db.init_app(app)
migrate = Migrate(app, db)

# Initialize login manager
login_manager = LoginManager()
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
