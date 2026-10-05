# Activity 1 - Encapsulation Review
|Class       |Protected state / invariant                   | Public operations          | 
|Patient     |_patient_id,_name;id and name cannot be empty | get_name(),get_patient_id()|
|Practitioner|_practitioner_id,_specialty;id non-empty unique|get_name(),get_specialty() |
|Appointment |_appt_id,_appt_datetime._status;datetime cannot be past for new scheduled appointment;status follow enum transition|cancel(),get_status(),get_datetime()|

# Activity 2 - Composition or Inheritance?
Appointment and Patient ->  Composition/association  Reason: Appointment associates with patient.Patient can exist independently, not is-a relationship.
Appointment and Practitioner ->  Composition/association  Reason: Appointment references practitioner;practioner exists without appointments.
Doctor and Practitioner (hypothetical) ->  Inheritance Reason: Doctor IS-A subtype of Practitioner.
Clinic and Appointment ->  Composition/association Reason: Clinic contains appointments,deleting clinic should not delet all appointment.

# Activity 3 - Responsibility Allocation
Who decides whether SCHEDULED can become CANCELLED?
The appointment domain object itself.

Who validates a patient name?
Patient class.

Should Appointment execute SQL? Why?
No.Appointment is pure domain business object.SQL persistence logic should go to seperate repository class.Mixing SQL breaaks separation-of-concerns and makes unit testing hand.

Should the UI decide whether a status transition is legal?
No.UI is presentation layer.Business state-transition rules belong inside domain Appointment object.If UI holds rules,different UI clients can behave inconsistently.

# Activity 4 - AI Code Critique
AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManagerdependency and inheritance from PatientRecord. Identify at least five design problems and corrections.
Problem: The AppointmentStatus enum contains COMPLETED, but there is no dedicated complete() method to safely handle this state transition. Status can only be changed by direct assignment.
Correction: Implement a complete() method. Check the current status; only SCHEDULED appointments can transition to COMPLETED or CANCELLED.
Problem: The cancel() method uses is not to compare Enum members. While sometimes working, is not is not the recommended operator for Enum comparison in Python.
Correction: Replace is not with != for comparing the AppointmentStatus enum values.
Problem: COMPLETED exists in enum but no complete() method for state transition.
Correction: Add complete() with state validation.
Problem: No check on initial status. Appointment can start as CANCELLED.
Correction: Add post_init to validate initial status must be SCHEDULED.
Problem: Risk of mixing database SQL code inside domain Appointment class. Violates single responsibility.
Correction: Move all database logic to separate repository class.

# Exit question
Why can code be object-oriented syntactically but still have poor object-oriented design?
Code may use OOP syntax like classes,objects,inheritance,but still break core OOP priciples.