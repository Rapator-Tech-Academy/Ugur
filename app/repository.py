from app import db

from app.models import UserModel

class Repository:

    def createUserRepo(self, data):
        u = UserModel(
            name = data.get("name"),
            surname = data.get("surname"),
            username = data.get("username"),
            mail = data.get("mail"),
            password = data.get("password")
        )
        db.session.add(u)
        db.session.commit()
    

    