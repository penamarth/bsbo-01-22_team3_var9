from application import Application
from grant_system_facade import GrantSystemFacade
from user import User


def main():
    facade = GrantSystemFacade()
    
    # Регистрация пользователей
    applicant = User("Иван Иванов", "ivan@example.com", "applicant", "password123")
    expert = User("Мария Петрова", "maria@example.com", "expert", "password456")
    fund_holder = User("Алексей Смирнов", "alexey@example.com", "fund_holder", "password789")
    
    applicant_id = facade.register(applicant)
    expert_id = facade.register(expert)
    fund_holder_id = facade.register(fund_holder)
    
    # Авторизация
    session_token = facade.login("ivan@example.com", "password123")
    
    # Подача заявки
    application = Application("Исследование AI", "Разработка инновационного AI", applicant_id)
    application_id = facade.submit_application(application)
    
    # Назначение эксперта и проведение экспертизы
    facade.assign_expert(application_id, expert_id)
    facade.evaluate_application(application_id, score=9.5, comments="Отличная заявка")
    
    # Принятие решения
    facade.make_decision(application_id, decision_type="Одобрено", reason="Высокая оценка эксперта")
    
    # Уведомления
    notifications = facade.get_notifications_by_user(applicant_id)
    for notification in notifications:
        print(notification.message)
    
    # Выход из системы
    facade.logout(applicant_id)

if __name__ == "__main__":
    main()