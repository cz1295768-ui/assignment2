# PartA
What data must be stored?
Patients' medical records and personal information,clinic doctors' schedule and personal information.
What functions might be useful?
Manage doctors' schedule, allow patients to make an appointment.
What could go wrong?
Empty patient or pracitioner name or email address.
What requirements are unclear?
How many users will use this system at the same time.

# PartC
## Prompt sent to CoPilot
Act as a Python tutor.I am learning introductory software technology.Here is a small appointment-booking function.1. Explain what the code does.2. Identify three limitations.3. Suggest improvements.4. Do not rewrite the whole application.5. Ask me two questions to test my understanding.

## AI Response
Here’s a clear, tutor‑style breakdown of your small appointment‑booking function. I’ll explain what it does, point out limitations, suggest improvements, and finish with two understanding‑check questions.
￼
🧩 1. What the code does
Even without seeing the exact snippet, an introductory appointment‑booking function typically:
• Stores basic appointment details — such as patient name, date, and time.
• Adds the appointment to a list — usually an in‑memory Python list.
• Checks simple conditions — for example, whether the time slot is empty.
• Allows cancellation — often by removing an item from the list.
In short, it manages appointments in a very direct, beginner‑friendly way: store → check → add/remove.
￼
⚠️ 2. Three limitations
Each item begins with a Guided Link so you can explore the idea further.
• No persistent storage — If the program stops, all appointments disappear because they live only in memory.
• No conflict handling — The function may not prevent double‑booking or overlapping times.
• Weak validation — It may accept invalid dates, empty names, or incorrectly formatted input.
These are common constraints in beginner programs.
￼
🔧 3. Suggested improvements
Not a rewrite — just conceptual upgrades.
• Add data persistence  
Save appointments to a file (JSON, CSV) or a small database so they survive program restarts.
• Introduce proper conflict checking  
Before adding an appointment, verify that the doctor and time slot are free.
• Improve validation  
Use Python’s 
datetime module to ensure dates and times are real and formatted correctly.
These changes keep your program small but make it more realistic.
￼
🎓 4. Two questions to test your understanding
1. If your program stores appointments only in a Python list, what happens when the program closes?
2. Why is checking for overlapping appointment times important in a real scheduling system?
￼
If you want, you can show me your actual function and I’ll walk you through it line by line using the same tutor style.

# PartD
## Prompt sent to CoPilot

Create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time. Do NOT use any database or GUI. Provide only core Python code with basic list storage.

### AI Response
A beginner‑friendly appointment function can be very small and still teach you the essentials of storing structured information. Here’s a clean, simple version that keeps everything in a Python list and uses only core language features — no database, no GUI, no external libraries.
￼
🌱 Simple Python Appointment Storage (Beginner Level)
# A list to store all appointments
appointments = []

def add_appointment(patient_name, practitioner_name, appointment_time):
    """Store a basic appointment as a dictionary."""
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)
    print("Appointment added successfully!")

# Example usage
add_appointment("Alice", "Dr. Smith", "2026-09-10 10:00")
add_appointment("Bob", "Dr. Lee", "2026-09-11 14:30")

print(appointments)

🧠 What this teaches you
• How to store structured data using a list of dictionaries
• How to build a simple function that adds items to a collection
• How to keep the program beginner‑friendly and readable
You can later expand this with features like appointment searching or basic conflict checking once you’re comfortable.
If you want, I can help you add cancellation, validation, or time‑format checking — all still beginner‑friendly and without rewriting the whole application.