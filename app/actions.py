import random

from stories import story, arguments, Success, Failure, Result

from app.factories import StudentFactory, StaffFactory, LessonFactory
from app.entities import BaseEntity, Student, Staff, Lesson
from app.repository import Repository, DeletingRepoData

student_factory = StudentFactory(Student)
Staff_factory = StaffFactory(Staff)
lesson_factory = LessonFactory(Lesson)
repo = Repository()
delete_user_data = DeletingRepoData()


class CreateStudent:

    @story
    @arguments("name", "surname", "age", "number")
    def run(I):
        I.validate_inputs
        I.build_entity
        I.persist
        I.done

    def validate_inputs(self, ctx):
        return Success()

    def build_entity(self, ctx):
        ctx.entity=student_factory.create(
            id=random.randint(0, 10000),
            name=ctx.name,
            surname=ctx.surname,
            age=ctx.age,
            number=ctx.number
        )

        return Success()

    def persist(self, ctx):
        ctx.result=repo.persist_instance(payload=ctx.entity.serialize())
        return Success()

    def done(self, ctx):
        return Result(ctx.entity.serialize())

class CreateStaff:

    @story
    @arguments("name", "surname", "age", "number", "salary")
    def run(I):
        I.validate_inputs
        I.build_entity
        I.persist
        I.done

    def validate_inputs(self, ctx):
        return Success()

    def build_entity(self, ctx):
        ctx.entity = Staff_factory.create(
            id=random.randint(0, 10000),
            name=ctx.name,
            surname=ctx.surname,
            age=ctx.age,
            number=ctx.number,
            salary=ctx.salary
        )
        return Success()

    def persist(self, ctx):
        ctx.result = repo.persist_instance(payload=ctx.entity.serialize())
        return Success()

    def done(self, ctx):
        return Result(ctx.entity.serialize())


class CreateLesson:

    @story
    @arguments("time", "type", "team")
    def run(I):
        I.validate_inputs
        I.build_entity
        I.persist
        I.done

    def validate_inputs(self, ctx):
        return Success()

    def build_entity(self, ctx):
        ctx.entity = lesson_factory.create(
            id=random.randint(0, 10000),
            time=ctx.time,
            type=ctx.type,
            team=ctx.team
        )
        return Success()

    def persist(self, ctx):
        ctx.result = repo.persist_instance(payload=ctx.entity.serialize())
        return Success()

    def done(self, ctx):
        return Result(ctx.entity.serialize())


class DeleteUser:

    @story
    @arguments("id")
    def run(I):
        I.checking_id
        I.deleting_data
        I.done

    def checking_id(self, ctx):
        ctx.outputdata = delete_user_data.check_user(id=ctx.id)
        if ctx.outputdata != None:
            return Success()
        return Failure()
    
    def deleting_data(self, ctx):
        delete_user_data.delete_data(outputdata=ctx.outputdata)
        return Success()
    
    def done(self, ctx):
        return Result(f'Deleted {ctx.id}')


    

    



