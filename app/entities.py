from dataclasses import dataclass

@dataclass
class User:
    name: str
    surname: str
    username: str
    mail: str
    password: str