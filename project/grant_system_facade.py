from application_manager import ApplicationManager
from auth_manager import AuthManager
from decision_manager import DecisionManager
from expertise_manager import ExpertiseManager
from notification_manager import NotificationManager


class GrantSystemFacade:
    def __init__(self):
        self.auth_manager = AuthManager()
        self.application_manager = ApplicationManager()
        self.expertise_manager = ExpertiseManager()
        self.decision_manager = DecisionManager()
        self.notification_manager = NotificationManager()

    def register(self, user):
        return self.auth_manager.register(user)

    def login(self, email, password):
        return self.auth_manager.login(email, password)

    def logout(self, user_id):
        self.auth_manager.logout(user_id)

    def submit_application(self, application):
        return self.application_manager.submit_application(application)

    def assign_expert(self, application_id, expert_id):
        self.expertise_manager.assign_expert(application_id, expert_id)

    def evaluate_application(self, application_id, score, comments):
        self.expertise_manager.evaluate_application(application_id, score, comments)

    def make_decision(self, application_id, decision_type, reason):
        self.decision_manager.make_decision(application_id, decision_type, reason)

    def get_notifications_by_user(self, user_id):
        return self.notification_manager.get_notifications_by_user(user_id)