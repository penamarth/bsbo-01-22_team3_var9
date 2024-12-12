```plantuml
@startuml

actor "FundHolder" as FH
actor "Applicant" as AP

participant "AuthManager" as AM
participant "ApplicationManager" as APM
participant "NotificationManager" as NM

== Основной успешный сценарий ==
AP -> AM : login(email, password)
activate AM
AM --> AP : Authenticated
deactivate AM

AP -> APM : fillApplication(Title, Description)
activate APM
APM --> AP : Application Form
deactivate APM

AP -> APM : submitApplication()
activate APM
APM -> APM : Create Applicant Object (ID, Title, Description, Status: "Under Review", Applicant: user)
APM --> AP : Application submitted (Status: "Under Review")
deactivate APM

APM -> NM : sendNotification(Notification)
activate NM
NM --> AP : Notify Applicant (Message: "Ваша заявка на грант успешно подана и находится на рассмотрении.", ApplicationID, Date)
deactivate NM

FH -> APM : getAllApplications()
activate APM
APM --> FH : List of Applications (ID, Title, Status)
deactivate APM

AP -> APM : getApplicationByID(UUID)
activate APM
APM --> AP : Application Details (ID, Title, Description, Status, Applicant)
deactivate APM

== Альтернативный сценарий 1: Ошибка при заполнении формы ==
AP -> APM : submitApplication()
activate APM
APM -> AP : Error Message (Missing fields)
deactivate APM

== Альтернативный сценарий 2: Отмена решения ==
AP -> APM : cancelApplication()
activate APM
APM --> AP : Return to main menu without saving data
deactivate APM

== Расширение: История поданных заявок ==
FH -> APM : getAllApplications()
activate APM
APM --> FH : List of Submitted Applications (Details for analysis)
deactivate APM

@enduml