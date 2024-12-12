import uuid


class Evaluation:
    def __init__(self, score: float, comments: str, expert_id: uuid.UUID):
        self.id = uuid.uuid4()
        self.score = score
        self.comments = comments
        self.expert_id = expert_id