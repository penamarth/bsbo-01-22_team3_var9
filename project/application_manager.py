import uuid
from typing import List, Optional

from application import Application


class ApplicationManager:
    def __init__(self):
        self.applications: List[Application] = []

    def submit_application(self, application: Application) -> uuid.UUID:
        self.applications.append(application)
        return application.id

    def update_application(self, application_id: uuid.UUID, updated_application: Application) -> None:
        for i, app in enumerate(self.applications):
            if app.id == application_id:
                self.applications[i] = updated_application
                return
        raise Exception(f"Application with ID {application_id} not found.")

    def delete_application(self, application_id: uuid.UUID) -> None:
        self.applications = [
            app for app in self.applications if app.id != application_id
        ]

    def get_application_by_id(self, application_id: uuid.UUID) -> Optional[Application]:
        for app in self.applications:
            if app.id == application_id:
                return app
        return None

    def get_all_applications(self) -> List[Application]:
        return self.applications