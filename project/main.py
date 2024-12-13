from application import Application
from expertise_manager import Evaluation
from grant_system_facade import GrantSystemFacade
from user import User


def main():
    # Инициализация фасада
    system = GrantSystemFacade()
    
    # --- 1. Регистрация пользователей ---
    applicant = User("Alice", "alice@example.com", "applicant", "password123")
    expert = User("Bob", "bob@example.com", "expert", "securepass")
    fund_holder = User("Charlie", "charlie@example.com", "fund_holder", "adminpass")
    
    # Регистрация пользователей
    applicant_id = system.register(applicant)
    expert_id = system.register(expert)
    fund_holder_id = system.register(fund_holder)
    print(f"Registered users: Applicant {applicant_id}, Expert {expert_id}, Fund Holder {fund_holder_id}")
    
    # --- 2. Логин и сессия ---
    session_token = system.login("alice@example.com", "password123")
    print(f"Alice logged in with session token: {session_token}")
    
    # --- 3. Создание и отправка заявки ---
    application = Application("Research Grant", "Research on AI", applicant)
    application_id = system.submit_application(application)
    print(f"Application submitted with ID: {application_id}")
    
    # --- 4. Назначение эксперта ---
    system.assign_expert(application_id, expert_id)
    print(f"Expert {expert_id} assigned to application {application_id}")
    
    # --- 5. Оценка заявки экспертом ---
    score = 85.5
    comments = "Great proposal, but needs minor improvements."
    system.evaluate_application(application_id, expert_id, score, comments)  # Передаем все три аргумента
    evaluation = system.get_evaluation(application_id)
    print(f"Evaluation completed: {evaluation.score}, Comments: {evaluation.comments}")
    
    # --- 6. Принятие решения ---
    decision_type = "Approved"
    reason = "High potential impact."
    system.make_decision(application_id, decision_type, reason)
    print(f"Decision made: {decision_type} for application {application_id}")
    
    # --- 7. Уведомления ---
    notification_message = f"Your application {application_id} has been reviewed and {decision_type.lower()}."
    system.send_notification(notification_message, applicant_id)
    notifications = system.get_notifications_by_user(applicant_id)
    print(f"Notifications for applicant: {[n.message for n in notifications]}")
    
    # --- 8. Платежи ---
    amount = 5000.0
    system.process_payment(application_id, amount)
    payment_status = system.get_payment_status(application_id)
    print(f"Payment status for application {application_id}: {payment_status}")
    
    # --- 9. Генерация отчетов ---
    report_title = "Application Review Summary"
    report_content = "Summary of the application process and outcomes."
    report = system.generate_report(report_title, report_content, fund_holder)
    print(f"Report generated: {report.title}, Content: {report.content}")
    
    # --- 10. Завершение ---
    system.logout(applicant_id)
    print(f"Alice logged out.")

if __name__ == "__main__":
    main()