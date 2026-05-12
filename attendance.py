students = ["Yaswanth", "Rahul", "Sai", "Kiran", "Abdin", "Pardhu"]

present_students = []

print("===== Smart Attendance System =====")

for student in students:
    
    attendance = input(f"Is {student} present? (yes/no): ")

    if attendance.lower() == "yes":
        present_students.append(student)

# Save attendance into file
file = open("attendance.txt", "w")

file.write("Present Students:\n")

for student in present_students:
    file.write(student + "\n")

file.close()

print("\nAttendance Saved Successfully!")