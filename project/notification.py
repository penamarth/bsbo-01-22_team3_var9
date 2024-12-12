
import uuid
from datetime import datetime


class Notification:
    def __init__(self, message: str, recipient_id: uuid.UUID):
        self.id = uuid.uuid4()
        self.message = message
        self.recipient_id = recipient_id
        self.date = datetime.now()