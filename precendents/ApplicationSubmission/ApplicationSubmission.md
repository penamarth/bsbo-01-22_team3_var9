# ApplicationSubmission.md

## Прецедент: "Подача заявки на грант"

Информационная система технической экспертизы.

---

## Уровень
Задача, определенная системой.

---

## Основной исполнитель
**Заявитель (Аpplicant)**

---

## Заинтересованные лица и их требования

### 1. Заявитель (Аpplicant)
- Возможность заполнения и подачи заявки на грант.
- Получение подтверждения о получении заявки.
- Прозрачность в процессе оценки заявки.

### 2. Держатель фонда (FundHolder)
- Доступ к поданным заявкам для дальнейшей оценки.
- Возможность отслеживания статуса заявок.

### 3. Эксперт (Expert)
- Получение заявок для проведения оценки.
- Возможность оставлять комментарии и рекомендации по заявкам.

### 4. Администратор системы
- Контроль корректности всех операций.
- Логирование всех действий системы для аудита.

---

## Предусловия
1. Заявитель зарегистрирован в системе и имеет активный аккаунт.
2. Заявитель ознакомился с условиями и требованиями для подачи заявки на грант.

---

## Результаты (Постусловия)
1. Заявка успешно подана и сохранена в системе со статусом "На рассмотрении".
2. Заявитель получает уведомление о подтверждении подачи заявки через `NotificationManager::sendNotification`.
3. Заявка доступна для экспертизи держателю фонда и экспертам через `ExpertiseManager::evaluateApplication`

---

## Основной успешный сценарий

### 1. Заполнение формы заявки
- Заявитель входит в систему через `AuthManager::login(email, password)`.
- Заявитель заполняет форму заявки, включая такие поля, как:
  - `Title`: название проекта.
  - `Description`: подробное описание проекта.

### 2. Подача заявки
- После устранения всех ошибок, заявитель нажимает кнопку "Подать заявку".
- Система создает объект `Applicant`, который включает:
  - `ID`: уникальный идентификатор заявки.
  - `Title`: название проекта.
  - `Description`: подробное описание проекта.
  - `Status`: статус заявки("На рассмотрении")
  - `Applicant`: пользователи.
- Система передает объект `Applicant` через `ApplicationManager::submitApplication`.

### 3. Уведомление о подтверждении
- Система отправляет уведомление заявителю через `NotificationManager::sendNotification(notification)`.
- `Notification` включает:
  - `Message`: сообщение о том, что заявка успешно подана ("Ваша заявка на грант успешно подана и находится на рассмотрении.").
  - `ApplicationID`: уникальный идентификатор заявки для отслеживания статуса.
  - `Date`: дата подачи заявки.
  - `Recipient`: заявитель.

### 4. Доступ к заявке для держателя фонда и экспертов
- Заявка становится доступной для просмотра держателю фонда через `ApplicationManager::getAllApplications()`, который возвращает список всех поданных заявок со статусами.

### 5. Доступ к заявке для пользователя
- Заявка становится доступной для просмотра `ApplicationManager::getApplicationByID(UUID)`, который получает ID заявки и возврщает объект `Applicant`:
  - `ID`: уникальный идентификатор заявки.
  - `Title`: название проекта.
  - `Description`: подробное описание проекта.
  - `Status`: статус заявки("На рассмотрении")
  - `Applicant`: пользователь.

---

## Варианты альтернативных решений

### 1. Ошибка при заполнении формы
- Если заявитель не заполнил обязательные поля:
  - Система отображает сообщение об ошибке с указанием недостающих полей.

### 2. Отмена решения
- Если заявитель решает отменить процесс подачи:
  - Система возвращает его к главному меню без сохранения данных заявки.

---

## Расширения

### 1. История поданных заявок
- Все решения сохраняются и доступны для анализа через `ApplicationManager::getAllApplications`.

---

## Специальные требования
1. Все данные о поданных заявках фиксируются в системе с минимальной задержкой (до 5 секунд).
2. Уведомления о статусе заявки отправляются немедленно после ее обработки.
3. Данные заявителей защищены в соответствии с законодательством (например, GDPR).

---

## Связь
1. **ApplicationManager**
    - Используется для управления данными заявок (`getApplicationByID`, `validateApplication`, `submitApplication`).
2. **AuthrManager** 
    - Предоставляет функции для управления пользователями и их доступом.
3. **NotificationManager**
    - Отправляет уведомления заявителям через `sendNotification`.