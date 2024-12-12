```plantuml
@startuml

actor "Expert" as EX
actor "FundHolder" as FH
actor "Applicant" as AP

participant "ApplicationManager" as AM
participant "ExpertiseManager" as EM
participant "NotificationManager" as NM
participant "ReportManager" as RM

== Основной успешный сценарий ==
EX -> AM : getApplicationByID(applicationID)
activate AM
AM --> EX : Application (ID, Title, Description, Status, Applicant)
deactivate AM

EX -> EM : startEvaluation(applicationID)
activate EM
EM -> EM : Assign criteria, weights, and forms
EM --> EX : Evaluation form generated
deactivate EM

EX -> EM : submitEvaluation(applicationID, Evaluation)
activate EM
EM -> EM : Save Evaluation (Scores, Comments)
EM --> EX : Evaluation submitted
deactivate EM

EM -> NM : notifyHolder(fund_id, message)
activate NM
NM -> FH : Notify FundHolder (Message: "Evaluation completed")
deactivate NM

== Альтернативный сценарий 1: Недостаток информации ==
EX -> AM : requestAdditionalInfo(applicationID, comment)
activate AM
AM -> AP : Notify Applicant (Message: "Additional info required")
deactivate AM

AP -> AM : submitAdditionalInfo(applicationID, info)
activate AM
AM --> EX : Additional information submitted
deactivate AM

EX -> EM : continueEvaluation(applicationID)
activate EM
EM --> EX : Continue with evaluation
deactivate EM

== Альтернативный сценарий 2: Сбой сохранения оценки ==
EX -> EM : submitEvaluation(applicationID, Evaluation)
activate EM
EM -> EM : Error saving evaluation
EM --> EX : Evaluation not saved
deactivate EM

EX -> NM : notifyAdmin(issue)
activate NM
NM -> FH : Notify Administrator (Issue: "Evaluation save failed")
deactivate NM

== Альтернативный сценарий 3: Эксперт хочет изменить ранее сохранённую оценку ==
EX -> EM : openEvaluation(applicationID)
activate EM
EM -> EM : Check if evaluation is editable
EM --> EX : Evaluation form unlocked
EX -> EM : submitUpdatedEvaluation(applicationID, updatedEvaluation)
EM -> EM : Save updated evaluation
EM --> EX : Evaluation updated
deactivate EM

== Расширения ==
== Расширение 1: Коллективная оценка ==
EX -> EM : startEvaluation(applicationID)
activate EM
EM -> EM : Assign group of experts
EM --> EX : Evaluation form for group
EX -> EM : submitEvaluation(applicationID, groupEvaluation)
deactivate EM

EM -> RM : generateReport("Evaluation results", parameters)
activate RM
RM --> FH : Report generated (Average scores, Comments)
deactivate RM

== Расширение 2: Анализ конфликта интересов ==
EM -> EM : Check for conflicts of interest
EM -> AM : IsExpertLinkedToApplicant(expertID, applicantID)
activate AM
AM --> EM : Conflict detected
EM -> EM : Reassign application to another expert
EM --> EX : Notification: "You have been assigned a new application due to conflict reassignment"
deactivate AM

@enduml
