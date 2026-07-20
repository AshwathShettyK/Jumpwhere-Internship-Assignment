# Q4: Determine the type of triangle based on its three sides.

try:
    side_a = float(input("Enter the first side of the triangle: "))
    side_b = float(input("Enter the second side of the triangle: "))
    side_c = float(input("Enter the third side of the triangle: "))
except ValueError:
    print("Invalid input. Please enter numeric values for the sides.")
    raise SystemExit

if side_a <= 0 or side_b <= 0 or side_c <= 0:
    print("Triangle sides must be greater than zero.")
elif side_a + side_b <= side_c or side_b + side_c <= side_a or side_c + side_a <= side_b:
    print("The entered sides do not form a valid triangle.")
elif side_a == side_b == side_c:
    print("The triangle is Equilateral.")
elif side_a == side_b or side_b == side_c or side_c == side_a:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")
