import uuid
from typing import Dict, Optional

from evaluation import Evaluation


class IExpertiseManager:
    """
    Интерфейс для менеджера экспертизы.
    """
    def assign_expert(self, application_id: uuid.UUID, expert_id: uuid.UUID) -> None:
        raise NotImplementedError

    def evaluate_application(self, application_id: uuid.UUID, evaluation: Evaluation) -> None:
        raise NotImplementedError

    def get_evaluation(self, application_id: uuid.UUID) -> Optional[Evaluation]:
        raise NotImplementedError


class ExpertiseManager(IExpertiseManager):
    """
    Менеджер экспертизы, реализующий IExpertiseManager.
    """
    def __init__(self):
        # Хранение данных об оценках
        self.evaluations: Dict[uuid.UUID, Optional[Evaluation]] = {}

    def assign_expert(self, application_id: uuid.UUID, expert_id: uuid.UUID) -> None:
        """
        Назначает эксперта для обработки заявки.
        """
        if application_id in self.evaluations:
            raise Exception(f"Application {application_id} already assigned to an expert.")
        self.evaluations[application_id] = None  # Подготовка для оценки после назначения эксперта
        print(f"Expert {expert_id} assigned to application {application_id}")

    def evaluate_application(self, application_id: uuid.UUID, evaluation: Evaluation) -> None:
        """
        Оценивает заявку, только после предварительного назначения эксперта.
        """
        if application_id not in self.evaluations:
            raise Exception(f"No expert assigned to application ID {application_id}.")
        self.evaluations[application_id] = evaluation
        print(f"Evaluation added: {evaluation.score}, {evaluation.comments}")

    def get_evaluation(self, application_id: uuid.UUID) -> Optional[Evaluation]:
        """
        Возвращает текущую оценку по заявке.
        """
        evaluation = self.evaluations.get(application_id, None)
        if evaluation:
            print(f"Retrieved evaluation: {evaluation.score}, {evaluation.comments}")
        else:
            print("No evaluation found for application.")
        return evaluation