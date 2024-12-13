import uuid


class Decision:
    def __init__(self, decision_type: str, reason: str, application_id: uuid.UUID):
        self.id = uuid.uuid4()
        self.decision_type = decision_type  # Например, "Одобрено" или "Отклонено"
        self.reason = reason
        self.application_id = application_id