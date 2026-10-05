1. Problem and scope

The SmartCare community‑clinic currently using spreadsheets and paper records to manage patients and appointment data. This management style causing duplicate bookings, hard‑to‑find patient records, inconsistent appointment status, poor visibility of doctor to availability and no reliable appointment history.
Scope: build a simple software system to manage patient medical records, practitioner details and clinic appointment.
Out of scope: Online patient self‑booking, SMS verification, online payment, facial recognition

2. Stakeholders

|Stakeholder             |Need                                                                                                                             |Evidence 
|Patient                 |Have their appointment and personal details recorded accurately and reliably by clinic staff, reducing the risk of booking errors|clinic relies entirely on manual spreadsheets and paper recording. 
|GP/Healthcare practitioner| To easily view their own upcoming appointments to see their availability                                                      |limited visibility of practitioner availability is a known problem in this case study 
|Clinic manager          |To generate simple, basic operational reports about clinic appointments.                                                         |Difficulty producing basic operational reports is one of the stated problem. Management requests a simple system to support clinic‑level appointment management 
|Clinic receptionist     |Create, cancel and check appointment easily; have automated system to avoid human‑error‑caused duplicate bookings                |The clinic relies entirely on manual spreadsheets and paper records.Also human error creates duplicate bookings and other listed operational problems. 
|Software development team| Build a simple, maintainable software within defined scope                                                                     |Development team need to build a system that maintainable and easy to use 

3. Functional requirements

• FR‑01: The system should allow a receptionist to add a new patient record

• FR‑02: The system should allow a receptionist to search for a patient by patient ID

• FR‑03: The system should be able to store basic GP information

• FR‑04: The system should allow receptionists to create a new appointment for a patient.

• FR‑05: The system shall prevent duplicate bookings

• FR‑06: The system shall allow receptionist to cancel an appointment

• FR‑07: The system should keep cancelled appointments in the appointment history

• FR‑08: The system shall allow all GP to view their scheduled appointments

• FR‑09: The system shall allow GP to mark an appointment as completed

• FR‑10: The system shall show the status of each appointment(booked,cancelled,finished)

• FR‑11: The system shall list all appointments for a selected day

• FR‑12: The system shall produce a simple appointment summary report for clinic management.

4. Non‑Functional Requirements

• NFR‑01: The system should have some security/privacy policies to secure users' information

• NFR‑02: The system shall store all data in a database in clinic

• NFR‑03: Patient and appointment data should not be visible for unauthorised people

• NFR‑04: User interface shall be easy to understand with less than one hour of training for new receptionists

• NFR‑05: Only authorised software development personnel shall be permitted to modify the source code and deploy updates to the application

• NFR‑06: The system should run on a desktop computer and everyone who used this computer should be registered.

5. User Stories

• US‑01: As a patient, I want to check when my appointment will start, so that I can arrive clinic on time.

• US‑02: As a receptionist, I want to use system to create new appointment, so that I can replace manual paper‑based booking.

• US‑03: As a receptionist, I want to use system to cancel appointments, so that I can update records when patients cannot attend.

• US‑04: As a GP, I want to check my daily schedule, so that I can know when I need to meet my patients.

• US‑05: As a clinic manager, I want a basic appointment report, so that I can check clinic's booking activity.

• US‑06: As a receptionist, I want system to block duplicate bookings, so that I can avoid double‑booking the same time slot.

6. Acceptance Criteria
GIVEN: A patient with ID P001 is saved in the system
WHEN : A receptionist enters P001 into the patient search
THEN : The system display the patient's record

GIVEN: There is an existing appointment for GP Dr Ayin at 2:00pm
WHEN : A reception tries to book another patient into this time slot
THEN : The system rejects the new booking and shows a duplicate‑booking warning

GIVEN: An active appointment exists in the system
WHEN : A receptionist select to cancel this appointment
THEN : The appointment status changes to cancelled and stored in history

7. Assumptions and Open Questions

Assumption

• We assume only clinic staff can log in to the system

• We assume all appointments have a fixed ,standard duration

Open Questions

• Does the clinic require different user permission level?

• How many users may use this system at the same time?

8. AI Requirements Review Record
|AI suggestion                                                               |Evidence?| Decision| Reason                                         |Verification 
|Start with a Minimum Clinic System functions are included in the final scope|Yes      | Include |The clinic requires a simple small‑scale system |Verified by acceptance testing , to ensure no unrequired advanced 
|Unique patient ID confirm each have a unique ID                             |Yes      |Include  |The clinic needs Unique patient ID to locate patient records|Verified by functional test cases:create multiple patients and 
|Filters, sorting, search improvements can quickly locate target records.    |Yes      |Include  |These method can help receptionist locate patient records easier|Verified by usability,and functional testing,checking that staff 
|Cleaner UI                                                                  |Yes      |Include  |The clinic wants a simple system  
|Track appointment status                                                    |Yes      |Include  |The clinic reported a lack of reliable appointment history|Verified by test cases that create,cancel and complete appointments, then check whether status values update correctly