```plantuml
@startuml

actor "FundHolder" as FH
actor "Applicant" as AP
participant "AuthManager" as AM
participant "ApplicationManager" as APM
participant "ExpertiseManager" as EM
participant "DecisionManager" as DM
participant "NotificationManager" as NM

== Основной успешный сценарий ==
FH -> AM : login(email, password)
activate AM
AM --> FH : Authenticated
deactivate AM

FH -> APM : getApplicationByID(applicationID)
activate APM
APM --> FH : Application Details (ID, Title, Description, Status)
deactivate APM

FH -> EM : getEvaluation(applicationID)
activate EM
EM --> FH : Evaluation (Score, Comments, Expert)
deactivate EM

FH -> DM : makeDecision(applicationID, decision)
activate DM
DM -> DM : Create Decision Object (ID, DecisionType, Reason, Application)
DM --> FH : Decision made (ID, DecisionType)
deactivate DM

FH -> APM : updateApplication(applicationID, updatedApplication)
activate APM
APM --> FH : Application updated (New Status)
deactivate APM

FH -> NM : sendNotification(notification)
activate NM
NM --> AP : Notify Applicant (Message: "Ваше решение по заявке принято.", ApplicationID, Date)
deactivate NM

== Альтернативный сценарий 1: Пересмотр решения ==
FH -> DM : reviewDecision(applicationID)
activate DM
DM -> DM : Update Decision Object (New DecisionType)
DM --> FH : Decision reviewed (New DecisionType)
deactivate DM

FH -> APM : updateApplication(applicationID, updatedApplication)
activate APM
APM --> FH : Application updated (New Status)
deactivate APM

FH -> NM : sendNotification(notification)
activate NM
NM --> AP : Notify Applicant (Message: "Ваше решение по заявке пересмотрено.", ApplicationID, Date)
deactivate NM

== Альтернативный сценарий 2: Ошибка при принятии решения ==
FH -> DM : makeDecision(applicationID, decision)
activate DM
DM -> FH : Error Message (Unable to save decision)
deactivate DM

== Альтернативный сценарий 3: Ошибка при отправке уведомления ==
FH -> NM : sendNotification(notification)
activate NM
NM -> FH : Error Message (Unable to send notification)
deactivate NM

@enduml
