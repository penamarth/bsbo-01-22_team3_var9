import uuid


class Application:
    def __init__(self, title: str, description: str, applicant_id: uuid.UUID):
        self.id = uuid.uuid4()
        self.title = title
        self.description = description
        self.status = "Подано"  # Возможные статусы: "Подано", "На рассмотрении", "Одобрено", "Отклонено"
        self.applicant_id = applicant_id

    def update_status(self, new_status: str):
        self.status = new_status