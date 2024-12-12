import uuid
from typing import List

from notification import Notification


class NotificationManager:
    def __init__(self):
        self.notifications: List[Notification] = []

    def send_notification(self, message: str, recipient_id: uuid.UUID) -> None:
        notification = Notification(message, recipient_id)
        self.notifications.append(notification)

    def get_notifications_by_user(self, user_id: uuid.UUID) -> List[Notification]:
        return [n for n in self.notifications if n.recipient_id == user_id]