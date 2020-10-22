from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    surname = db.Column(db.String(40))
    age = db.Column(db.Integer)
    address = db.Column(db.Text)

    def __repr__(self):
        return f"[{self.id} User successfully added {self.name}]"