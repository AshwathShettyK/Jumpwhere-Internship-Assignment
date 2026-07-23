# Q12: Calculate attendance percentage and exam eligibility.

try:
    classes_held = int(input("Enter number of classes held: "))
    classes_attended = int(input("Enter number of classes attended: "))
except ValueError:
    print("Invalid input. Please enter integer values.")
    raise SystemExit

if classes_held <= 0:
    print("Number of classes held must be greater than zero.")
    raise SystemExit

attendance_percentage = (classes_attended / classes_held) * 100
print(f"Attendance percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam")
