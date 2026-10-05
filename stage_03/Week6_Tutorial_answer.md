# Candidate Concepts
|Candidate   |Class?|Reason
|Patient     |Yes   |Real-world business entity,stores patient personal information.
|Practitioner|Yes   |Real-world business entity,holds practitioner details.
|Appointment |Yes   |Core domain object thatrecords booking information.
|Name        |No    |It is an attribute,not a class It belongs to Patient or Practitioner.
|Clinic      |Yes   |Represents the clinic organisation in this domain.
|Database    |No    |It is a technical implementation component,not part of the domian model.
|Cancellation|No    |It is an operation,not a standalone class.It changes the state of Appointment.
|Status      |NO    |It is an attribute of Appointment,not a separate class.

# CRC Cards
Patient
|Responsibilities                                           |Collaborators
|Storew patient personal details;provide patient information|Appointment

Practitioner
|Responsibilities                                           |Collaborators
|Store practitioner details;Manage available time slots     |Appointment

Appointment
|Responsibilities                                                             |Collaborators
|Record booking details;Track appointment status;Link patient and practitioner|Patient,Practitioner

# Relationship Reasoning
Patient to Appointment: which relationship and why?
Relationship:Association (one‑to‑many)
One Patient can have many Appointments; each Appointment belongs to exactly one Patient.

Practitioner to Appointment: what multiplicity?
Practitioner 1 ←→ * Appointment
One practitioner can have many appointments, each appointment is assigned to exactly one practitioner.

Should Appointment inherit from Patient?
No. Inheritance means “is‑a”. An appointment is not a patient. Appointment associates with Patient, uses association，not inheritance.

Does Clinic need to own every object?
Not necessary. Clinic is the organisation, but Patient, Practitioner, Appointment exist as independent domain objects. Clinic does not need composition ownership over all of them.

# AI Model Critique
Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController,NotificationManager, ScheduleEngine.
|AI suggestion|Evidence|Decision     |Reason  |Model change|
|Make appointment as central class linking Patient and Practitioner|booking problem is the core business pain-point from the case study|Accept|Appointment is the core entity for the clinic's appointment-booking entity|Use appointment as central class connecting Patient and Practitioner.

|Add availability-Schedule as attribute inside Practitioner|Limited visibility of practitioner availability and duplicate booking are part of the clinic's problem|Modify|Keep the availbility-schedule but avoid strong full large-scale rosters to prevent data redundancy|Retain the availability attribute in Practitioner.Modify it to store lightweight availble time-slot data.

|Add billing/Invoice class|the clinic only requires a system to manage patients,practitioners and appointments,with no billing/invoice requirement for the system|Reject|Billing and invoice functionality is out of scope.|Keep only three core business classes:Patient,Practitoner and appointment.

|Add PatientManager,PractitionerManager,AppointmentManager,ClinicController,NotificationManager,ScheduleEngine|These are controller/service classes, not real‑world domain entities|Reject|Manager and Controller classes belong to implementation layer rather than domain model, should not appear in domain UML diagram|Remove all these manager‑style classes from domain model|