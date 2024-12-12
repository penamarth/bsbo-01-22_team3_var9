import uuid
from typing import Dict

from report import Report


class ReportManager:
    def __init__(self):
        self.reports: Dict[uuid.UUID, Report] = {}

    def generate_report(self, title: str, content: str, generated_by: uuid.UUID) -> Report:
        report = Report(title, content, generated_by)
        self.reports[report.id] = report
        return report

    def get_report_by_id(self, report_id: uuid.UUID) -> Report:
        return self.reports.get(report_id, None)