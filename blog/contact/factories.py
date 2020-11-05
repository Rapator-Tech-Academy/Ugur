from .entities import Contact

class ContactFactory:
    def __init__(self, builder):
        self.builder = builder
    
    def create(self, **kwargs):
        return self.builder(
            name = kwargs.get('name'),
            surname = kwargs.get('surname'),
            email = kwargs.get('email'),
            number = kwargs.get('number')
        )
