import uuid
from datetime import datetime


class Report:
    def __init__(self, title: str, content: str, generated_by: uuid.UUID):
        self.id = uuid.uuid4()
        self.title = title
        self.content = content
        self.generated_by = generated_by
        self.date = datetime.now()