# Requirement-to-Concept Trace
|Requirement              |Concept      |State/behaviour  |Decision
|Patient books appointment|Patient      |state            |keep as class
|Practitioner sees patient|Practitioner |state            |keep as class
|Booking record/time slot |Appointment  |state + behaviour|keep as class
|Cancellation             |-            |behaviour        |reject as class
|Name                     |Patient/Practitioner|state     |not a class
|Status                   |Appointment  |state            |not a class
|Database                 |-            |technical        |reject

# CRC Cards
Patient
|Responsibilities                                            |Collaborators
|store personal details;provide own information when booking |Appointment
Practitioner
|Responsibilities                                      |Collaborators
|store practitioner details;manage available time slots|Appointment
Appointment
|Responsibilities                                                         |Collaborators
|record booking details;track status;link one patient and one practitioner|Patient,Practitioner
Optional class
|Responsibilities                                                         |Collaborators
|record booking details;track status;link one patient and one practitioner|Patient,Practitioner

# Design Rationale
Explain class selection, responsibility allocation and key relationships.

I selected three core classes — Patient, Practitioner and Appointment — because they are the real-world business entities named directly in the requirements. Name and Status were treated as attributes rather than classes, and Database was excluded as a technical implementation detail. Cancellation is modelled as a behaviour/state change of Appointment, not a separate class. Patient and Practitioner connect to Appointment through a one-to-many association: one patient or practitioner may have many appointments, but each appointment belongs to exactly one of each. No inheritance is used because Appointment is not a kind of Patient; no strong composition is used because deleting the clinic must not delete historical patient and appointment records.

AI Design Review Record
|AI suggestion|Evidence|Decision     |Reason  |Model change|
|Make appointment as central class linking Patient and Practitioner|booking problem is the core business pain-point from the case study|Accept|Appointment is the core entity for the clinic's appointment-booking entity|Use appointment as central class connecting Patient and Practitioner.

|Add availability-Schedule as attribute inside Practitioner|Limited visibility of practitioner availability and duplicate booking are part of the clinic's problem|Modify|Keep the availbility-schedule but avoid strong full large-scale rosters to prevent data redundancy|Retain the availability attribute in Practitioner.Modify it to store lightweight availble time-slot data.

|Add billing/Invoice class|the clinic only requires a system to manage patients,practitioners and appointments,with no billing/invoice requirement for the system|Reject|Billing and invoice functionality is out of scope.|Keep only three core business classes:Patient,Practitoner and appointment.