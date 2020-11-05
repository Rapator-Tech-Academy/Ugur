from stories import Success, Failure, Result, story, arguments

from .entities import Contact
from .factories import ContactFactory
from .repository import Repository

class CreateContactInfo:

    @story
    @arguments('name', 'surname', 'email', 'number')
    def create(I):
        I.validate_inputs
        I.build_entity
        I.persist_data
        I.done
    
    def validate_inputs(self, ctx):
        return Success()

    def build_entity(self, ctx):
        ctx.entity_factory = ContactFactory(builder=Contact)
        ctx.entity = ctx.entity_factory.create(
            name = ctx.name,
            surname = ctx.surname,
            email = ctx.email,
            number = ctx.number
        )
        return Success()
    
    def persist_data(self, ctx):
        ctx.new_info = Repository().create_customer_info(payload=ctx.entity)
        return Success()

    def done(self, ctx):
        return Result(ctx.new_info)