```plantuml
@startuml
actor "FundHolder" as FH
actor "Applicant" as AP

participant "ApplicationManager" as AM
participant "ExpertiseManager" as EM
participant "DecisionManager" as DM
participant "PaymentManager" as PM
participant "NotificationManager" as NM
participant "ReportManager" as RM

== Основной успешный сценарий ==
FH -> AM : getApplicationByID(applicationID)
activate AM
AM --> FH : Application (ID, Title, Description, Status, Applicant)
deactivate AM

FH -> EM : getEvaluation(applicationID)
activate EM
EM --> FH : Evaluation (Score, Comments, Expert)
deactivate EM

FH -> DM : makeDecision(applicationID, Decision)
activate DM
DM -> DM : Save Decision (Type: "Approved", Reason)
DM --> FH : Decision saved
deactivate DM

DM -> AM : updateApplication(applicationID, updatedApplication)
activate AM
AM --> DM : Application updated (Status: "Approved")
deactivate AM

DM -> PM : processPayment(applicationID, amount)
activate PM
PM -> PM : Initiate Payment Transaction
PM --> DM : Payment processed (Status: "Successful")
deactivate PM

DM -> NM : sendNotification(Notification)
activate NM
NM -> AP : Notify Applicant (Message: "Your application has been approved. The grant will be transferred shortly.")
deactivate NM

FH -> RM : generateReport("Approved Grants", parameters)
activate RM
RM -> AM : getAllApplications(Status: "Approved")
activate AM
AM --> RM : List of approved applications
deactivate AM

RM -> DM : getDecisions(applicationID)
activate DM
DM --> RM : Decision details (Reason, Comments)
deactivate DM

RM --> FH : Report generated (Details of approved grants)
deactivate RM

== Ошибка 1: Обработка платежа ==
DM -> PM : processPayment(applicationID, amount)
activate PM
PM -> PM : Payment transaction failed
PM --> DM : Payment failed (Status: "Failed")
deactivate PM

DM -> NM : sendNotification(Notification)
activate NM
NM -> AP : Notify Applicant (Message: "Payment processing delayed. We will resolve this issue shortly.")
deactivate NM

DM -> RM : logIssue("Payment error for applicationID")
activate RM
RM --> DM : Issue logged
deactivate RM

== Ошибка 2: Отмена решения ==
FH -> DM : reviewDecision(applicationID)
activate DM
DM -> DM : Revert Decision
DM --> FH : Decision reverted
deactivate DM

DM -> AM : updateApplication(applicationID, updatedApplication)
activate AM
AM --> DM : Application updated (Status: "Under Review")
deactivate AM

DM -> NM : sendNotification(Notification)
activate NM
NM -> AP : Notify Applicant (Message: "Your application is under review again.")
deactivate NM

== Ошибка 3: Отправка уведомления ==
DM -> NM : sendNotification(Notification)
activate NM
NM -> NM : Notification sending failed
NM --> DM : Notification failed
deactivate NM

DM -> RM : logIssue("Notification error for applicationID")
activate RM
RM --> DM : Issue logged
deactivate RM

== Ошибка 4: Обновление статуса заявки ==
DM -> AM : updateApplication(applicationID, updatedApplication)
activate AM
AM -> AM : Error updating application status
AM --> DM : Update failed
deactivate AM

DM -> NM : sendNotification(Notification)
activate NM
NM -> AP : Notify Applicant (Message: "There was an issue updating your application. Please wait for resolution.")
deactivate NM

DM -> RM : logIssue("Application update error for applicationID")
activate RM
RM --> DM : Issue logged
deactivate RM

@enduml