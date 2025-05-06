from app import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash
import json

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    matches = db.relationship('Match', backref='owner', lazy='dynamic')
    shared_with_me = db.relationship('SharedAnalysis', 
                                     foreign_keys='SharedAnalysis.shared_with_id',
                                     backref='shared_with', 
                                     lazy='dynamic')
    shared_by_me = db.relationship('SharedAnalysis', 
                                   foreign_keys='SharedAnalysis.shared_by_id',
                                   backref='shared_by', 
                                   lazy='dynamic')
    
    def set_password(self, password): # TODO: Add unittest 
        self.password_hash = generate_password_hash(password)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    opponent = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Match score fields
    user_score = db.Column(db.String(20), nullable=True)
    opponent_score = db.Column(db.String(20), nullable=True)
    match_result = db.Column(db.String(10), nullable=True)  # 'win', 'loss', 'draw' # better use enum?
    
    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relationships
    statistics = db.relationship('MatchStatistic', backref='match', lazy='dynamic', cascade="all, delete-orphan")
    shared = db.relationship('SharedAnalysis', backref='match', lazy='dynamic', cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Match {self.title} - {self.date}>'

class MatchStatistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    statistic_type = db.Column(db.String(50), nullable=False)
    statistic_data = db.Column(db.Text, nullable=False)  # JSON string of the statistic data
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign keys
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    
    def get_data(self):
        """Returns the statistic data as a Python dictionary."""
        return json.loads(self.statistic_data)
    
    def set_data(self, data_dict):
        """Sets the statistic data from a Python dictionary."""
        self.statistic_data = json.dumps(data_dict)
    
    def __repr__(self):
        return f'<MatchStatistic {self.statistic_type} for Match {self.match_id}>'

class SharedAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shared_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign keys
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    shared_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    shared_with_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f'<SharedAnalysis Match {self.match_id} shared by {self.shared_by_id} with {self.shared_with_id}>'
