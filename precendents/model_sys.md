```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontSize 12
skinparam classFontName Arial
skinparam classBackgroundColor LightYellow
skinparam classBorderColor Black
skinparam packageBackgroundColor LightBlue
skinparam packageBorderColor Black

' --- Интерфейсы ---

interface IAuthManager {
  +register(user: User): UUID
  +login(email: String, password: String): String
  +logout(userID: UUID): void
  +validateSession(sessionToken: String): User
}

interface IApplicationManager {
  +submitApplication(application: Application): UUID
  +updateApplication(applicationID: UUID, updatedApplication: Application): void
  +deleteApplication(applicationID: UUID): void
  +getApplicationByID(applicationID: UUID): Application
  +getAllApplications(): List<Application>
}

interface IExpertiseManager {
  +assignExpert(applicationID: UUID, expertID: UUID): void
  +evaluateApplication(applicationID: UUID, evaluation: Evaluation): void
  +getEvaluation(applicationID: UUID): Evaluation
}

interface IDecisionManager {
  +makeDecision(applicationID: UUID, decision: Decision): void
  +reviewDecision(applicationID: UUID): void
}

interface INotificationManager {
  +sendNotification(notification: Notification): void
  +getNotificationsByUser(userID: UUID): List<Notification>
}

interface IPaymentManager {
  +processPayment(applicationID: UUID, amount: Decimal): void
  +getPaymentStatus(applicationID: UUID): String
}

interface IReportManager {
  +generateReport(reportType: String, parameters: Map<String, Object>): Report
  +getReportByID(reportID: UUID): Report
}

' --- Фасад ---
class GrantSystemFacade {
  +ApplicationManager: IApplicationManager
  +ExpertiseManager: IExpertiseManager
  +DecisionManager: IDecisionManager
  +NotificationManager: INotificationManager
  +PaymentManager: IPaymentManager
  +ReportManager: IReportManager
  +submitApplication(data: Application): UUID
  +makeDecision(applicationID: UUID, decision: Decision): void
  +sendNotification(notification: Notification): void
  +generateReport(reportType: String, parameters: Map<String, Object>): Report
  +register(user: User): UUID
  +login(email: String, password: String): String
  +logout(userID: UUID): void
}

' --- Основные классы ---
class ApplicationManager implements IApplicationManager {
  +Applications: List<Application>
  +submitApplication(application: Application): UUID
  +updateApplication(applicationID: UUID, updatedApplication: Application): void
  +deleteApplication(applicationID: UUID): void
  +getApplicationByID(applicationID: UUID): Application
  +getAllApplications(): List<Application>
}

class ExpertiseManager implements IExpertiseManager {
  +Evaluations: Map<UUID, Evaluation>
  +assignExpert(applicationID: UUID, expertID: UUID): void
  +evaluateApplication(applicationID: UUID, evaluation: Evaluation): void
  +getEvaluation(applicationID: UUID): Evaluation
}

class DecisionManager implements IDecisionManager {
  +makeDecision(applicationID: UUID, decision: Decision): void
  +reviewDecision(applicationID: UUID): void
}

class NotificationManager implements INotificationManager {
  +Notifications: List<Notification>
  +sendNotification(notification: Notification): void
  +getNotificationsByUser(userID: UUID): List<Notification>
}

class PaymentManager implements IPaymentManager {
  +Payments: Map<UUID, Payment>
  +processPayment(applicationID: UUID, amount: Decimal): void
  +getPaymentStatus(applicationID: UUID): String
}

class ReportManager implements IReportManager {
  +Reports: List<Report>
  +generateReport(reportType: String, parameters: Map<String, Object>): Report
  +getReportByID(reportID: UUID): Report
}

class AuthManager implements IAuthManager {
  +Sessions: Map<String, User>
  +register(user: User): UUID
  +login(email: String, password: String): String
  +logout(userID: UUID): void
  +validateSession(sessionToken: String): User
}

' --- Пользователи ---
class User {
  +ID: UUID
  +Name: String
  +Email: String
  +Role: String
  +Password: String [encrypted]
}

class Applicant {
  +Applications: List<Application>
}

class Expert {
  +AssignedApplications: List<Application>
  +Evaluations: List<Evaluation>
}

class FundHolder {
  +Decisions: List<Decision>
}

' --- Другие классы ---
class Application {
  +ID: UUID
  +Title: String
  +Description: String
  +Status: String
  +Applicant: User
}

class Evaluation {
  +ID: UUID
  +Score: Decimal
  +Comments: String
  +Expert: User
}

class Decision {
  +ID: UUID
  +DecisionType: String
  +Reason: String
  +Application: Application
}

class Notification {
  +ID: UUID
  +Message: String
  +Recipient: User
  +Date: Date
}

class Payment {
  +ID: UUID
  +Amount: Decimal
  +Status: String
  +Date: Date
}

class Report {
  +ID: UUID
  +Title: String
  +Content: String
  +GeneratedBy: User
  +Date: Date
}

' --- Связи ---
GrantSystemFacade o-- IApplicationManager
GrantSystemFacade o-- IExpertiseManager
GrantSystemFacade o-- IDecisionManager
GrantSystemFacade o-- INotificationManager
GrantSystemFacade o-- IPaymentManager
GrantSystemFacade o-- IReportManager
GrantSystemFacade o-- IAuthManager

Applicant --> IApplicationManager : submits application
ApplicationManager o-- Application : manages >
ExpertiseManager o-- Evaluation : manages >
DecisionManager o-- Decision : manages >
NotificationManager o-- Notification : manages >
PaymentManager o-- Payment : manages >
ReportManager o-- Report : manages >
AuthManager o-- User : manages sessions

User "1" -- "*" Application : submits >
Expert "1" -- "*" Evaluation : performs >
FundHolder "1" -- "*" Decision : makes >
Notification "*" -- "1" User : sent to >
Payment "1" -- "1" Application : for >
Report "*" -- "1" User : generated by >
@enduml
