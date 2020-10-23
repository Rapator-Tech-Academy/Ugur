from app import db

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class UserModel(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    surname = db.Column(db.String(40))
    username = db.Column(db.String(40))
    mail = db.Column(db.String(40))
    hashed_password = db.Column(db.String)

    def __repr__(self):
        return f"{self.id} User created {self.name}"
    
    def generate_password(self, password):
        self.hashed_password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    
