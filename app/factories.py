
class UserFactory:
    def __init__(self, builder):
        self.builder = builder

    def create(self, **kwargs):
        return self.builder(
            name = kwargs.get("name"),
            surname = kwargs.get("surname"),
            username = kwargs.get("username"),
            mail = kwargs.get("mail"),
            password = kwargs.get("password")
        )