# PartE
|Question                     |Human version          |AI version        |
|Easy to understand?          |Yes                    |Yes               |
|Runs successfully?           |Yes                    |Yes               |
|Uses only required features? |Yes                    |Yes               |
|Adds assumptions?            |No                     |No                |
|Handles errors?              |No                     |No                |
|Could I explain it?          |Yes                    |Yes               |

# PartF
1. **Normal appointment**
Human result: Appointment stored successfully and can be displayed.
AI result: Appointment stored successfully and can be displayed.

2. **Blank patient name**
Human result: Blank name will be printed directly, no error rejection.
AI result: Accepts blank name and stores invalid appointment data.

3. **Two appointments for the same practitioner/time**
Human result: Duplicate time bookings are allowed, no warning or conflict check.
AI result: Duplicate time bookings are allowed, no warning or conflict check.

4. **Strange input such as patient_name=None or appointment_time=None**
Human result: None value will be printed directly, no error handling.
AI result: None values are directly stored into appointment records with no checks.
