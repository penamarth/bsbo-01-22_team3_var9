from application_manager import ApplicationManager
from auth_manager import AuthManager
from decision_manager import DecisionManager
from expertise_manager import ExpertiseManager
from notification_manager import NotificationManager
from payment_manager import PaymentManager
from report_manager import ReportManager


class GrantSystemFacade:
    def __init__(self):
        self.auth_manager = AuthManager()
        self.application_manager = ApplicationManager()
        self.expertise_manager = ExpertiseManager()
        self.decision_manager = DecisionManager()
        self.notification_manager = NotificationManager()
        self.payment_manager = PaymentManager()
        self.report_manager = ReportManager()

    # --- Методы аутентификации ---
    def register(self, user):
        return self.auth_manager.register(user)

    def login(self, email, password):
        return self.auth_manager.login(email, password)

    def logout(self, user_id):
        self.auth_manager.logout(user_id)

    # --- Методы для работы с заявками ---
    def submit_application(self, application):
        return self.application_manager.submit_application(application)

    def update_application(self, application_id, updated_application):
        self.application_manager.update_application(application_id, updated_application)

    def delete_application(self, application_id):
        self.application_manager.delete_application(application_id)

    def get_application_by_id(self, application_id):
        return self.application_manager.get_application_by_id(application_id)

    def get_all_applications(self):
        return self.application_manager.get_all_applications()

    # --- Методы для работы с экспертизой ---
    def assign_expert(self, application_id, expert_id):
        self.expertise_manager.assign_expert(application_id, expert_id)

    def evaluate_application(self, application_id, expert_id, score, comments):
        self.expertise_manager.evaluate_application(application_id, expert_id, score, comments)

    def get_evaluation(self, application_id):
        return self.expertise_manager.get_evaluation(application_id)

    # --- Методы для работы с решениями ---
    def make_decision(self, application_id, decision_type, reason):
        self.decision_manager.make_decision(application_id, decision_type, reason)

    def review_decision(self, application_id):
        return self.decision_manager.review_decision(application_id)

    # --- Методы для работы с уведомлениями ---
    def send_notification(self, message, recipient_id):
        self.notification_manager.send_notification(message, recipient_id)

    def get_notifications_by_user(self, user_id):
        return self.notification_manager.get_notifications_by_user(user_id)

    # --- Методы для работы с платежами ---
    def process_payment(self, application_id, amount):
        return self.payment_manager.process_payment(application_id, amount)

    def get_payment_status(self, application_id):
        return self.payment_manager.get_payment_status(application_id)

    # --- Методы для работы с отчетами ---
    def generate_report(self, title, content, generated_by):
        return self.report_manager.generate_report(title, content, generated_by)

    def get_report_by_id(self, report_id):
        return self.report_manager.get_report_by_id(report_id)

    # --- Исправление ошибки вызова метода evaluate_application в main.py ---
    def evaluate_application(self, application_id, expert_id, score, comments):
        if not expert_id or not comments:
            raise ValueError("Both expert_id and comments must be provided.")
        self.expertise_manager.evaluate_application(application_id, expert_id, score, comments)
