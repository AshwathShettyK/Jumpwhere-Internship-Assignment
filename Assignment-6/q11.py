# Q11: Assign grade based on marks.

try:
    marks = float(input("Enter the marks: "))
except ValueError:
    print("Invalid input. Please enter a numeric value for marks.")
    raise SystemExit

if marks < 0 or marks > 100:
    print("Marks should be between 0 and 100.")
elif marks < 25:
    grade = "F"
elif marks < 45:
    grade = "E"
elif marks < 50:
    grade = "D"
elif marks < 60:
    grade = "C"
elif marks < 80:
    grade = "B"
else:
    grade = "A"

print(f"Grade: {grade}")
