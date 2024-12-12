```plantuml
@startuml
actor "FundHolder" as FH
actor "Applicant" as AP

participant "ApplicationManager" as AM
participant "ExpertiseManager" as EM
participant "DecisionManager" as DM
participant "NotificationManager" as NM
participant "ReportManager" as RM

== Основной успешный сценарий ==

FH -> AM : getApplicationByID(applicationID)
activate AM
AM --> FH : Application (ID, Title, Description, Status)
deactivate AM

FH -> EM : getEvaluation(applicationID)
activate EM
EM --> FH : Evaluation (Score, Comments)
deactivate EM

FH -> DM : makeDecision(applicationID, Decision)
activate DM
DM -> DM : Save Decision (Type: "Rejected", Reason)
DM --> FH : Decision saved
deactivate DM

DM -> AM : updateApplication(applicationID, updatedApplication)
activate AM
AM --> DM : Application updated (Status: "Rejected")
deactivate AM

DM -> NM : sendNotification(Notification)
activate NM
NM -> AP : Notify Applicant (Message: "Your application was rejected")
deactivate NM

DM -> RM : generateReport("Rejections", parameters)
activate RM
RM --> FH : Report (Rejected applications summary)
deactivate RM

== Альтернативный сценарий: Ошибка сохранения решения ==

FH -> DM : makeDecision(applicationID, Decision)
activate DM
DM -> DM : Error during saving
DM --> FH : Error message
deactivate DM

== Альтернативный сценарий: Уведомление не доставлено ==

DM -> NM : sendNotification(Notification)
activate NM
NM -> NM : Error during sending
NM --> DM : Notification failed
deactivate NM

DM -> RM : logIssue("Notification error for applicationID")
activate RM
RM --> DM : Issue logged
deactivate RM

== Расширение: Генерация отчета для всех отклоненных заявок ==

FH -> RM : generateReport("RejectedApplications", parameters)
activate RM
RM -> AM : getAllApplications(Status: "Rejected")
activate AM
AM --> RM : List of rejected applications
deactivate AM

RM -> DM : getDecisions(applicationID)
activate DM
DM --> RM : Decision details (Reason, Comments)
deactivate DM

RM --> FH : Full report on rejected applications
deactivate RM

@enduml