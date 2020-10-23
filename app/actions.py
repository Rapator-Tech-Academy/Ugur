from stories import story, arguments, Success, Failure, Result

from app.entities import User
from app.factories import UserFactory

class CreateUser:

    @story
    @arguments("name", "surname", "username", "email", "password")
    def create(I):
        I.validate_inputs
        I.build_entity
        I.repo_add
        I.done
    
    def validate_inputs(self, ctx):
        return Success()
    
    def build_entity(self, ctx):
        ctx.entity_factory = UserFactory(data=User)
        ctx.entity = ctx.entity_factory.serialize(
            name = ctx.name,
            surname = ctx.surname,
            username = ctx.username,
            mail = ctx.mail,
            password = ctx.password
        )
        return Success()
    
    def repo_add(self, ctx):
        return Success()

    def done(self, ctx):
        return Success()