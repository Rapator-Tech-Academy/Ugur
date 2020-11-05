from .models import ContactModel

class Repository:

    def create_customer_info(self, payload):
        info = ContactModel.objects.create(
            name = payload.name,
            surname = payload.surname,
            email = payload.email,
            number = payload.number
        )


