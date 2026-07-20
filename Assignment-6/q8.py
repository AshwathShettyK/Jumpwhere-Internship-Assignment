# Q8: Check whether the rectangle is a square.

try:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    raise SystemExit

if length <= 0 or breadth <= 0:
    print("Length and breadth must be greater than zero.")
elif length == breadth:
    print("The rectangle is a square.")
else:
    print("The rectangle is not a square.")
