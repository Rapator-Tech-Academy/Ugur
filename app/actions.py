from stories import story, arguments, Success, Failure, Result

from app.factories import UserFactory
from app.entities import User

class CreateUser:

    @story
    @arguments("name", "surname", "age", "address")
    def create(I):
        I.validate_inputs
        I.build_entity
        I.persist_user
        I.done
    
    def validate_inputs(self, ctx):
        name_validation = isinstance(ctx.name, str)
        surname_validation = isinstance(ctx.surname, str)
        age_validation = isinstance(ctx.age, int)
        address_validation = isinstance(ctx.address, str)

        if name_validation and surname_validation and age_validation and address_validation:
            return Success()
        else:
            return Failure()
    
    def build_entity(self, ctx):
        ctx.entity_factory = UserFactory(builder=User)
        ctx.entity = ctx.entity_factory.create(
            name = ctx.name,
            surname = ctx.surname,
            age = ctx.age,
            address = ctx.address
        )
        return Success()
    
    def persist_user(self, ctx):
        ctx.result = self.repo.createUser(payload=ctx.entity)
        return Success()

    def done(self, ctx):
        return Result(ctx.result)
