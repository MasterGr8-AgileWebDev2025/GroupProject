from app import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
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
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'
