class StudentFactory:
    def __init__(self, builder):
        self.builder = builder

    def create(self, **kwargs):
        return self.builder(
            id=kwargs.get("id"),
            name=kwargs.get("name"),
            surname=kwargs.get("surname"),
            age=kwargs.get("age"),
            number=kwargs.get("number")
        )


class StaffFactory:
    def __init__(self, builder):
        self.builder = builder

    def create(self, **kwargs):
        return self.builder(
            id = kwargs.get("id"),
            name=kwargs.get("name"),
            surname=kwargs.get("surname"),
            age=kwargs.get("age"),
            number = kwargs.get("number"),
            salary=kwargs.get("salary")
        )


class LessonFactory:
    def __init__(self, builder):
        self.builder = builder

    def create(self, **kwargs):
        return self.builder(
            id = kwargs.get("id"),
            time=kwargs.get("time"),
            type=kwargs.get("type"),
            team=kwargs.get("team")
        )



