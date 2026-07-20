# Q10: Calculate bonus and total salary based on years of service.

try:
    salary = float(input("Enter the salary: "))
    years_of_service = float(input("Enter years of service: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    raise SystemExit

if salary < 0 or years_of_service < 0:
    print("Salary and years of service must be non-negative.")
    raise SystemExit

bonus = 0
if years_of_service > 5:
    bonus = salary * 0.05

total_salary = salary + bonus

print(f"Bonus amount: {bonus}")
print(f"Total salary after bonus: {total_salary}")
