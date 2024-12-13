import uuid

from user import User


class AuthManager:
    def __init__(self):
        self.users = {}
        self.sessions = {}

    def register(self, user):
        user_id = uuid.uuid4()
        self.users[user_id] = user
        return user_id

    def login(self, email, password):
        for user_id, user in self.users.items():
            if user.email == email and user.password == password:
                session_token = str(uuid.uuid4())
                self.sessions[session_token] = user_id
                return session_token
        raise Exception("Invalid credentials")

    def logout(self, user_id):
        self.sessions = {k: v for k, v in self.sessions.items() if v != user_id}