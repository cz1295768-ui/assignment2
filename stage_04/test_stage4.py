from patient import Patient
from practitioner import Practitioner
from appointment import Appointment, AppointmentStatus
from datetime import datetime

def test_patient_validation():
    p1 = Patient(patient_id="P001", name="Alice", contract="public")
    print("Patient valid test passed")

    try:
        p2 = Patient(patient_id="   ", name="Bob", contract="public")
        print("FAIL: Should have raised error for empty patient_id")
    except ValueError as e:
        print(f"Patient id check passed: {e}")

    try:
        p3 = Patient(patient_id="P002", name="   ", contract="public")
        print("FAIL: Should have raised error for empty name")
    except ValueError as e:
        print(f"Patient name check passed: {e}")


def test_appointment_cancel():
    app = Appointment(
        appID=1,
        dateTime=datetime(2026,10,1,14,30),
        _status=AppointmentStatus.SCHEDULED
    )

    app.cancel()
    assert app.status == AppointmentStatus.CANCELLED
    print("Cancel test passed")

    try:
        app.cancel()
        print("FAIL: Cancelling cancelled appointment should fail")
    except ValueError as e:
        print(f"Cancel rule test passed: {e}")


if __name__ == "__main__":
    test_patient_validation()
    test_appointment_cancel()