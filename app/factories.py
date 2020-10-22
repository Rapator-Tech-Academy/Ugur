class UserFactory:
    def __init__(self, builder):
        self.builder = builder
    
    def create(self, **kwargs):
        return self.builder(
            name = kwargs.get("name"),
            surname = kwargs.get("surname"),
            age = kwargs.get("age"),
            address = kwargs.get("address")
        )