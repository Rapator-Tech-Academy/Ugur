class BaseEntity:
    def __init__(self, id, name, surname, age, number):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number

    def serialize(self):
        return { 
            self.id : {
                "name" : self.name,
                "surname" : self.surname,
                "age" : self.age,
                "number" : self.number
                }
        }


class Student(BaseEntity):
    pass


class Staff(BaseEntity):
    def __init__(self, salary, **kwargs):
        self.salary = salary
        super().__init__(**kwargs)

    def serialize(self):
        return {
            self.id : {
                "name" : self.name,
                "surname" : self.surname,
                "age" : self.age,
                "number" : self.number,
                "salary" : self.salary
                }
        }



class Lesson:
    def __init__(self, id, time, type, team):
        self.id = id
        self.time = time
        self.type = type
        self.team = team

    def serialize(self):
        return {
            self.id : {
                "time" : self.time,
                "type" : self.type,
                "team" : self.team
            }
        }


