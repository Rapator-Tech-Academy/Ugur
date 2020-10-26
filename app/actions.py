from app.repository import Repository
from stories import story, arguments, Success, Failure, Result

from app.entities import User
from app.factories import UserFactory


class CreateUser:

    @story
    @arguments("name", "surname", "username", "mail", "password")
    def create(I):
        I.validate_inputs
        I.build_entity
        I.add_userdata
        I.done
    
    def validate_inputs(self, ctx):
        return Success()
    
    def build_entity(self, ctx):
        ctx.entity_factory = UserFactory(builder=User)
        ctx.entity = ctx.entity_factory.create(
            name = ctx.name,
            surname = ctx.surname,
            username = ctx.username,
            mail = ctx.mail,
            password = ctx.password
        )
        return Success()
    
    def add_userdata(self, ctx):
        ctx.result = Repository().createUserRepo(data=ctx.entity)
        return Success()

    def done(self, ctx):
        return Result(ctx.result)