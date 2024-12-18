# Словарь терминов

## История изменений

| Версия | Дата         | Описание                                               | Автор         |
|--------|--------------|--------------------------------------------------------|---------------|
| 1.0    | 12 декабря 2024 | Начальный черновик глоссария на основе модели предметной области | asfqx   |

## Определения

| Термин              | Определение                                                                                                        | Формат                        | Правило верификации                                            | Синоним                  |
|---------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------|-----------------------------------------------------------------|--------------------------|
| **Пользователь**    | Индивид, взаимодействующий с информационной системой технической экспертизы, включающий Заявителей, Экспертов, Держателя фонда и администраторов. | Сущность с уникальным ID      | Должен иметь уникальный UUID, действительный email и защищённый пароль | -                        |
| **Соискатель гранта**  | Индивид, который подает заявку на грант, следит за её статусом и взаимодействует с экспертами и держателями фонда.   | Подкласс Пользователя         | Должен быть зарегистрирован и аутентифицирован в системе        | Заявитель                |
| **Независимый эксперт**     | Специалист, оценивающий заявки на гранты, принимающий решения о их одобрении или отказе, а также пересматривающий ранее принятые решения. | Подкласс Пользователя         | Должен быть зарегистрирован в системе и иметь соответствующую квалификацию | Эксперт                  |
| **Держатель фонда**         | Лицо или организация, управляющие фондом, предоставляющим гранты, принимающие окончательные решения о выдаче средств. | Подкласс Пользователя         | Должен быть зарегистрирован и аутентифицирован в системе       | Финансовый управляющий    |
| **Подача заявки**           | Процесс, в ходе которого соискатель гранта формирует и отправляет заявку на получение финансирования.             | Процесс                       | Должен быть завершён с корректно заполненными полями заявки    | -                        |            |
| **Оценка заявки**           | Процесс анализа и оценки поданной заявки независимым экспертом для принятия решения о её одобрении или отказе.     | Процесс                       | Должен основываться на критериях оценки, установленных системой | -                        |
| **Принятие решения/пересмотр решения** | Процесс принятия окончательного решения о заявке, включая возможность пересмотра ранее принятого решения.        | Процесс                       | Должен основываться на результатах оценки и внутренней политике фонда | -                        |            
| **Просмотр статуса заявки** | Возможность для соискателя гранта отслеживать текущее состояние своей заявки в системе.                             | Процесс                       | Должен отображать актуальную информацию о статусе заявки       | -                        |
| **Отказ**                   | Официальное решение о непринятии заявки на грант, сообщаемое соискателю.                                          | Процесс                       | Должен сопровождаться объяснением причин отказа               | -                        |
| **Выдача**                  | Процесс передачи средств соискателю гранта после одобрения заявки.                                                | Процесс                       | Должен быть завершён с учетом всех финансовых и юридических требований | -                        |
| **Служба авторизации**      | Компонент системы, отвечающий за проверку идентификации пользователей и управление доступом к системе.              | Служба                        | Должна обеспечивать безопасность данных пользователей          | -                        |
| **Экспертиза**             | Процесс оценки качества и соответствия заявок установленным критериям и стандартам.                               | Процесс                       | Должна включать независимых экспертов с соответствующими квалификациями | -                        |
| **Бухгалтерия**            | Отдел или система, отвечающая за финансовые операции, включая выдачу грантов и учёт расходов.                       | Отдел/Система                 | Должна вести учёт всех финансовых транзакций                   | -                        |
| **Система уведомления**     | Компонент системы, отвечающий за отправку уведомлений пользователям о статусе их заявок и других важных событиях.  | Система                       | Должна обеспечивать своевременную и корректную отправку уведомлений  | -                        |