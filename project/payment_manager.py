import uuid
from typing import Dict

from payment import Payment


class PaymentManager:
    def __init__(self):
        self.payments: Dict[uuid.UUID, Payment] = {}

    def process_payment(self, application_id: uuid.UUID, amount: float) -> Payment:
        if application_id in self.payments:
            raise Exception(f"Payment for application ID {application_id} already exists.")
        payment = Payment(application_id, amount, status="Completed")
        self.payments[application_id] = payment
        return payment

    def get_payment_status(self, application_id: uuid.UUID) -> str:
        payment = self.payments.get(application_id)
        if not payment:
            return "No Payment Found"
        return payment.status