```plantuml
@startuml
actor "Applicant" as AP
actor "FundHolder" as FH

participant "AuthManager" as AM
participant "ApplicationManager" as APM
participant "NotificationManager" as NM
participant "ReportManager" as RM

== Основной успешный сценарий ==

AP -> AM : login(email, password)
activate AM
AM --> AP : Authenticated
deactivate AM

AP -> APM : getApplicationByID(applicationID)
activate APM
alt Application found
    APM --> AP : Application (ID, Title, Description, Status)
    
    alt Status changed
        AP -> NM :sendNotification(notification: Notification)
        activate NM
        NM -> AP : Notify (Message: "Статус вашей заявки изменился.")
        deactivate NM
    else Status not changed
    end
else Application not found
    APM --> AP : Error (Message: "Заявка с указанным ID не найдена.")
end
deactivate APM

AP -> RM : getApplicationByID(invalidID)
activate RM
RM --> AP : Request logged (UserID, Action, Date)
deactivate RM

== Альтернативный сценарий 1: Заявка не найдена ==
AP -> APM : getApplicationByID(invalidID)
activate APM
APM --> AP : Error (Message: "Заявка с указанным ID не найдена.")
deactivate APM

== Альтернативный сценарий 2: Ошибка отправки уведомления ==
APM -> NM :sendNotification(notification: Notification)
activate NM
NM -> NM : Notification sending failed
NM --> APM : Error (Message: "Failed to send notification.")
deactivate NM

== Расширение: Просмотр нескольких заявок ==
AP -> APM : getAllApplications()
activate APM
APM --> AP : List of Applications (IDs, Titles, Statuses)
deactivate APM

@enduml
