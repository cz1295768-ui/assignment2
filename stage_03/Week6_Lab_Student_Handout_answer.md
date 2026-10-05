# A - Requirements Review
Highlight nouns, verbs and business rules in SmartCare v0.2.
### Nouns
Patient, Practitioner(GP), Appointment, Clinic, Patient records, Appointment status, Practitioner availability, Appointment history, Operational reports, Spreadsheets, Paper records

### Verbs
manage, book, locate, cancel, produce, store, view, record

### Business Rules
1. Prevent duplicate appointment bookings.
2. Keep consistent appointment status information.
3. Support viewing practitioner availability.
4. Support automated appointment cancellation.
5. Maintain reliable appointment history.
6. Generate basic operational reports.
7. The system must be simple; it should NOT be a complex hospital‑information system, suitable for a small community clinic.
8. Replace fragmented manual paper‑based and spreadsheet‑based workflows.

# B Candidate Classes
Record candidate concepts, supporting requirements, state and behaviour.

# C - CRC Cards
Create CRC cards for Patient, Practitioner and Appointment
Patient
|Responsibilities                                            |Collaborators
|store personal details;provide own information when booking |Appointment
Practitioner
|Responsibilities                                      |Collaborators
|store practitioner details;manage available time slots|Appointment
Appointment
|Responsibilities                                                         |Collaborators
|record booking details;track status;link one patient and one practitioner|Patient,Practitioner

# E - AI Design Review
Ask AI to suggest classes and relationships using only confirmed requirements; require supporting requirementIDs.
Here’s a clean, requirement‑driven class model for the **SmartCare v1 system**, using **only the confirmed requirements** you provided.  
Each class includes **requirement IDs** showing exactly which requirement justifies its existence or attributes.

---

## 🎯 Core Classes (Derived Only from Confirmed Requirements)

### **1. Patient**  
Supports locating patient records, storing basic info, and linking to appointments.





**Requirement IDs:** R2 (locating records), R6 (appointment history)

**Attributes**
- patientId  
- name  
- dateOfBirth  
- contactDetails  

**Relationships**
- **Patient 1..* — Appointment** (R6)

---

### **2. Practitioner**  
Supports visibility of practitioner availability and prevents double‑booking.





**Requirement IDs:** R4 (visibility of availability), R1 (duplicate bookings)

**Attributes**
- practitionerId  
- name  
- specialty  
- availabilitySchedule  

**Relationships**
- **Practitioner 1..* — Appointment** (R1, R4)

---

### **3. Appointment**  
Central class addressing booking, status, cancellation, history, and reporting.





**Requirement IDs:**  
R1 (duplicate bookings)  
R3 (status consistency)  
R5 (cancellation process)  
R6 (history)  
R7 (reporting)

**Attributes**
- appointmentId  
- dateTime  
- status (Booked / Completed / Cancelled)  
- cancellationReason (optional)  

**Relationships**
- **Appointment *..1 — Patient** (R6)  
- **Appointment *..1 — Practitioner** (R1, R4)

---

## 📐 Class Diagram (Textual)

```
Patient (R2, R6)
 └─ patientId
 └─ name
 └─ dateOfBirth
 └─ contactDetails
        |
        | 1..*
        |
Appointment (R1, R3, R5, R6, R7)
 └─ appointmentId
 └─ dateTime
 └─ status
 └─ cancellationReason
        |
        | *..1
        |
Practitioner (R1, R4)
 └─ practitionerId
 └─ name
 └─ specialty
 └─ availabilitySchedule
```

---

## 📌 Why These Classes Are Valid  
Every class and relationship is justified **only** by the confirmed requirements:

| Requirement | Class Impact |
|------------|--------------|
| **R1: Duplicate bookings** | Practitioner–Appointment relationship; appointment time validation |
| **R2: Difficulty locating patient records** | Patient class with searchable fields |
| **R3: Inconsistent appointment status** | Appointment.status attribute |
| **R4: Limited visibility of practitioner availability** | Practitioner.availabilitySchedule |
| **R5: Manual cancellation process** | Appointment.cancellationReason + status |
| **R6: Lack of reliable appointment history** | Patient–Appointment & Practitioner–Appointment |
| **R7: Difficulty producing reports** | Appointment as central reporting entity |

---

## 🧭 Next Step  
If you want, I can generate **use‑case diagrams**, **sequence diagrams**, or a **database schema** based strictly on these requirements.  

Would you like to explore **use cases**, **database tables**, or **UML sequence flows** next?


# F - Compare and Decide
Record at least one accepted, modified and rejected AI suggestion.
|AI suggestion|Evidence|Decision     |Reason  |Model change|
|Make appointment as central class linking Patient and Practitioner|booking problem is the core business pain-point from the case study|Accept|Appointment is the core entity for the clinic's appointment-booking entity|Use appointment as central class connecting Patient and Practitioner.

|Add availability-Schedule as attribute inside Practitioner|Limited visibility of practitioner availability and duplicate booking are part of the clinic's problem|Modify|Keep the availbility-schedule but avoid strong full large-scale rosters to prevent data redundancy|Retain the availability attribute in Practitioner.Modify it to store lightweight availble time-slot data.

|Add billing/Invoice class|the clinic only requires a system to manage patients,practitioners and appointments,with no billing/invoice requirement for the system|Reject|Billing and invoice functionality is out of scope.|Keep only three core business classes:Patient,Practitoner and appointment.
# Reflection
What modelling decision was hardest? 
The hardest decision was deciding whether to model practitioner availability as an attribute or a separate class. Creating a new class for availability would add extra complexity, but storing it only as an attribute risks limited visibility for booking checks. I finally chose an attribute inside Practitioner to keep the domain model simple and within project scope.

Where did AI over-design? 
AI suggested many manager and controller‑style classes such as PatientManager and ScheduleEngine. These are implementation‑level service classes, they are not real‑world domain concepts. Adding them would over‑engineer the domain model. AI also proposed a billing/invoice class which was outside the given case‑study requirements.

What evidence supported your final choices?
All final design choices are based directly on the case‑study requirements. Only real‑world business entities (Patient, Practitioner, Appointment) are kept in domain model. Evidence includes the booking‑duplication problem, appointment‑status tracking requirement, and the fact that billing functions were not mentioned in requirements. I also followed domain‑modelling rules to exclude controller/manager technical classes.