
class UserFactory:
    def __init__(self, data):
        self.data = data

    def serialize(self, **kwargs):
        return self.data(
            name = kwargs.get("name"),
            surname = kwargs.get("surname"),
            username = kwargs.get("username"),
            mail = kwargs.get("mail"),
            password = kwargs.get("password")
        )