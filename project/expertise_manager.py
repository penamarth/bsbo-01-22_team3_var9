import uuid
from typing import Dict, Optional

from evaluation import Evaluation


class ExpertiseManager:
    def __init__(self):
        self.evaluations: Dict[uuid.UUID, Evaluation] = {}

    def assign_expert(self, application_id: uuid.UUID, expert_id: uuid.UUID) -> None:
        if application_id in self.evaluations:
            raise Exception(f"Application with ID {application_id} already assigned to an expert.")
        self.evaluations[application_id] = None  # Резервируем место для оценки

    def evaluate_application(self, application_id: uuid.UUID, evaluation: Evaluation) -> None:
        if application_id not in self.evaluations:
            raise Exception(f"No expert assigned to application ID {application_id}.")
        self.evaluations[application_id] = evaluation

    def get_evaluation(self, application_id: uuid.UUID) -> Optional[Evaluation]:
        return self.evaluations.get(application_id, None)