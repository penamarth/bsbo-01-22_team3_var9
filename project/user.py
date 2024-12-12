import uuid


class User:
    def __init__(self, name: str, email: str, role: str, password: str):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.role = role
        self.password = password