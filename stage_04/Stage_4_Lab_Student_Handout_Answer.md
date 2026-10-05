# E - Review Generated Code
Check model consistency, unsupported features, public state mutation, unnecessary inheritance, inventeddependencies and error handling.
Patient valid test passed
Patient id check passed: Patient id cannot be empty
Patient name check passed: Patient name cannot be empty
Cancel test passed
Cancel rule test passed: Illegal state transition: cannot cancel appointment with statusCANCELLED


# H - AI Engineering Log
Record prompt, generated contribution, decisions and verification evidence.
prompt:
Implement only the Appointment class and AppointmentStatus enum.
Do NOT create any other classes such as Person.
Appointment attributes: appID:int, dateTime:datetime, status:AppointmentStatus
Enum AppointmentStatus values: SCHEDULED, CANCELLED, COMPLETED
Implement cancel() method:
Only appointments with status SCHEDULED can be cancelled.
If cancel() is called when status is not SCHEDULED, raise an exception for illegal state transition.
Use Python type hints.
No database logic, no save/load functions.

generated contribution:
from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"


@dataclass
class Appointment:
    appID: int
    dateTime: datetime
    status: AppointmentStatus

    def cancel(self) -> None:
        if self.status is not AppointmentStatus.SCHEDULED:
           raise ValueError(
               f"Illegal state transition: cannot cancel appointment with status {self.status.name}"
)

        self.status = AppointmentStatus.CANCELLED

decisions and verification evidence:
|AI contribution   | Conforms? | Decision | Reason | Verification |
|cancel() method using is not for Enum comparison|No|Accept with modification|!= is standard for Enum comparison. Replace is not with !=|Run test cases for cancel state check|
|Public status attribute in Appointment dataclass|No|Accept with modification|Public state mutation risk. Change to private _status with @property read-only access|Attempt direct assignment to status, expect error|
|Appointment class + AppointmentStatus Enum|Yes|Accept with modification|Matches updated UML, no database logic, no unnecessary inheritance, implements business rule for cancel|Manual behaviour test, compare against UML diagram|


# Reflection
Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI?
I modified two AI-generated parts: replaced is not with != for Enum comparison, and made status private with a read-only property to maintain encapsulation.
The approved UML and business rules constrained AI. AI must follow the predefined class structure and state rules instead of adding inappropriate logic.
