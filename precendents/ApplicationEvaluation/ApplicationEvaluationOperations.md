# ApplicationEvaluationOperations.md

## Описание системных операций

Данный документ описывает системные операции, необходимые для реализации прецедента "Оценка заявки". Каждая операция связана с компонентами диаграммы классов и включает в себя подробные шаги выполнения, предусловия, действия и результаты.

---

### **1. Операция: getApplicationByID(applicationID: UUID)**

#### **Ссылка**
- **Прецедент:** Оценка заявки.
- **Компонент:** ApplicationManager.

#### **Предусловия**
1. Заявка существует в системе.
2. Пользователь (Эксперт) аутентифицирован и имеет права доступа к заявкам.

#### **Действия**
1. ApplicationManager принимает applicationID в качестве аргумента.
2. Метод getApplicationByID извлекает объект Application из хранилища.
3. Система возвращает объект заявки с атрибутами:
   - ID: Уникальный идентификатор заявки.
   - Title: Название заявки.
   - Description: Описание заявки.
   - Status: Текущий статус заявки.
   - Applicant: Ссылка на пользователя-заявителя.

#### **Постусловия**
- Объект заявки успешно извлечен для последующей обработки.

---

### **2. Операция: getEvaluation(applicationID: UUID)**

#### **Ссылка**
- **Прецедент:** Оценка заявки.
- **Компонент:** ExpertiseManager.

#### **Предусловия**
1. Экспертная оценка заявки существует в системе.
2. Эксперт аутентифицирован и имеет доступ к заявке.

#### **Действия**
1. ExpertiseManager принимает applicationID в качестве аргумента.
2. Метод getEvaluation извлекает объект Evaluation, связанный с заявкой.
3. Система возвращает объект Evaluation:
   - Score: Результат оценки.
   - Comments: Комментарии эксперта.
   - Expert: Эксперт, проводивший оценку.

#### **Постусловия**
- Объект оценки успешно извлечен для анализа или редактирования.

---

### **3. Операция: evaluateApplication(applicationID: UUID, evaluation: Evaluation)**

#### **Ссылка**
- **Прецедент:** Оценка заявки.
- **Компонент:** ExpertiseManager.

#### **Предусловия**
1. Эксперт аутентифицирован в системе.
2. Заявка доступна для оценки.

#### **Действия**
1. Метод evaluateApplication принимает:
   - applicationID: Идентификатор заявки.
   - evaluation: Объект оценки.
2. ExpertiseManager проверяет корректность данных оценки (например, баллы находятся в пределах допустимого диапазона).
3. Оценка сохраняется в системе, заявка помечается как "Оценена".

#### **Постусловия**
- Результаты оценки сохранены в базе данных.
- Заявка обновлена в системе со статусом "Оценена".

---

### **4. Операция: sendNotification(notification: Notification)**

#### **Ссылка**
- **Прецедент:** Оценка заявки.
- **Компонент:** NotificationManager.

#### **Предусловия**
1. Оценка заявки завершена.
2. Уведомление сформировано системой.

#### **Действия**
1. Метод sendNotification принимает объект Notification с атрибутами:
   - Message: Текст уведомления.
   - Recipient: Получатель (Держатель фонда).
   - Date: Дата отправки.
2. NotificationManager отправляет уведомление через настроенный канал связи (например, e-mail или SMS).

#### **Постусловия**
- Уведомление успешно доставлено держателю фонда.
- Лог операции сохранен в системе.

---

### **5. Операция: updateApplication(applicationID: UUID, updatedApplication: Application)**

#### **Ссылка**
- **Прецедент:** Оценка заявки.
- **Компонент:** ApplicationManager.

#### **Предусловия**
1. Заявка существует в системе.
2. Обновленные данные заявки доступны.

#### **Действия**
1. Метод updateApplication принимает:
   - applicationID: Идентификатор заявки.
   - updatedApplication: Объект с обновленными данными заявки.
2. ApplicationManager обновляет заявку в базе данных.

#### **Постусловия**
- Заявка успешно обновлена.
- Лог изменений сохранен в системе.


#### Общие замечания:

- Все действия фиксируются в логах через ReportManager.
- В случае ошибок уведомления об ошибке отправляются администратору через NotificationManager.
- Связь объектов (заявки, оценки, эксперты, уведомления) осуществляется по уникальным идентификаторам.