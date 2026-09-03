# Copilot generated python
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment1 = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment1)

book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")

print(appointments)