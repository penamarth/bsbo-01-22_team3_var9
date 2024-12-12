import uuid
from typing import Dict, Optional

from decision import Decision


class DecisionManager:
    def __init__(self):
        self.decisions: Dict[uuid.UUID, Decision] = {}

    def make_decision(self, application_id: uuid.UUID, decision: Decision) -> None:
        if application_id in self.decisions:
            raise Exception(f"Decision for application ID {application_id} already exists.")
        self.decisions[application_id] = decision

    def review_decision(self, application_id: uuid.UUID) -> Optional[Decision]:
        return self.decisions.get(application_id, None)