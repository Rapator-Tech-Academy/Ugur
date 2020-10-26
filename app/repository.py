from app import db

from app.models import UserModel

class Repository:

    def createUserRepo(self, data):
        user = UserModel(
            name = data.name,
            surname = data.surname,
            username = data.username,
            mail = data.mail,
        )
        user.generate_password(password=data.password)

        db.session.add(user)
        db.session.commit()
    

    