# PartA Client Brief: AI-OFF
The SmartCare-clinic currently using spreadsheets and paper records to manage patients and appointment data. This management style causing duplicate bookings, hard‑to‑find patient data, inconsistent appointment status, poor visibility of doctor availability, and no reliable appointment history. Build a simple software system to manage patient medical records, practitioner details and clinic appointment.

# PartB Stakeholders and Scope: AI OFF
1. stakeholders
|Patient | Need: Have their appointment and personal details recorded accurately and reliably by clinic staff; reducing the risk of booking errors

|GP/Healthcare practitioner | Need: To easily view their own upcoming appointments to see their availability

|Clinic manager | Need: Monitor clinic‑wide bookings, check reports

|Clinic receptionist | Need: Create, cancel and check appointment easily; have automated system to avoid human-error-caused duplicate bookings

|Software development team | Need:

2. In-scope / Out-of-scope / Provisional features
Confirmed(In-scope):

Receptionists create appointments

Practitioners view schedules

Cancelled appointments remain in history

Out of scope:

Facial recognition login

Online payment

AI recommends treatments

Assumption requiring validation(Provisional):

Patients receive SMS reminders



# PartC Functional requirements 

• FR‑01: add new patient record

• FR‑02: search patient by patient ID

• FR‑03: store basic GP information

• FR‑04: receptionist create new appointment for patient

• FR‑05: prevent duplicate bookings

• FR‑06: receptionist cancel an appointment

• FR‑07: keep cancelled appointments in appointment history

• FR‑08: allow GP view their scheduled appointments

• FR‑09: mark appointment as completed

• FR‑10: show status of each appointment

• FR‑11: list all appointments for a selected day

• FR‑12: produce simple appointment summary report for clinic management

# PartD Non-Functional requirements


• NFR‑01: security & privacy to protect user data

• NFR‑02: patient‑appointment data stored in database

• NFR‑03: patient appointment data invisible for unauthorised people

• NFR‑04: UI easy to understand

• NFR‑05: new reception staff can learn system within less than one‑hour training

• NFR‑06: system runs on desktop computer, registered users can modify source code and deploy updates

# PartE User Stories and Acceptance Criteria:

1. User Stories
US‑01: As a patient, I want to check when my appointment will start, so that I can arrive clinic on time.
US‑02: As a receptionist, I want to use system to create new appointments, so that I can replace manual paper‑based booking.
US‑03: As a receptionist, I want to use system to cancel appointments, so that I can update records when patients cannot attend.
US‑04: As a GP, I want to check my daily schedule, so that I can know when I need to meet my patients.
US‑05: As a clinic manager, I want a basic appointment report, so that I can check clinic’s booking activity.
US‑06: As a receptionist, I want system to block duplicate bookings, so that I can avoid double‑booking the same time slot.

2. Acceptance Criteria

US‑01: A patient when ID P001 is saved in the system
GIVEN: A receptionist enters P001 into the patient search
THEN: The system display the patient’s record
US‑02:
GIVEN: There is an existing appointment for Dr Aylin at 2:00pm
WHEN: A receptionist tries to book another patient into this time slot
THEN: The system rejects the new booking and shows a duplicate‑booking warning
US‑03:
GIVEN: An active appointment exists in the system
WHEN: A receptionist select to cancel this appointment
THEN: The appointment status changes to cancelled and stored in history

Part G — AI Requirements Review Record
|AI suggestion                           |Evidence?|Decision |Reason                                         | Verification 
|Start with a Minimum Clinic System (MCS)| Yes     |Include  |The clinic requires a simple small‑scale system|Verified by acceptance testing, to ensure no unrequired advanced functions are included in the final scope 
|Unique patient ID                       |Yes      |Include  |The clinic needs Unique patient ID to locate patient records|Verified by functional test case:create multiple patients and confirm each have a unique ID 
|Filters, sorting, search improvements   |Yes      |Include  |These method can help receptionist locate patient records easier|Verified by usability and functional testing, checking that staff can quickly locate target records. 
|Cleaner UI Assumption requiring validation|No     |Defer    |The case study just mention system needs to be simple, but didn’t mention a "cleaner UI"|We need to consult clinic staff to define measurable usability standards for the user interface. 
|Track appointment status                |Yes      |Include  |The clinic reported a lack of reliable appointment history|Verified by test cases that create,cancel and complete appointments,then check whether status values update correctly 

