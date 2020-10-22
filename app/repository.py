from app import db
from app.models import User

class Repository:
    
    def createUser(self, payload):
        new_user = User(
            name = payload.name,
            surname = payload.surname,
            age = payload.age,
            address = payload.address
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    def get_all_user(self):
        return User.query.all()

