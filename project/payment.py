import uuid
from datetime import datetime


class Payment:
    def __init__(self, application_id: uuid.UUID, amount: float, status: str = "Pending"):
        self.id = uuid.uuid4()
        self.application_id = application_id
        self.amount = amount
        self.status = status  # Возможные статусы: "Pending", "Completed", "Failed"
        self.date = datetime.now()