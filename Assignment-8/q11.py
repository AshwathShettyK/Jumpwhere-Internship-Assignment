# Q11: Lambda functions for addition and multiplication.

add_fifteen = lambda x: x + 15
multiply = lambda x, y: x * y

try:
    number = float(input("Enter a number to add 15: "))
    print(f"Result: {add_fifteen(number)}")

    a = float(input("Enter the first number to multiply: "))
    b = float(input("Enter the second number to multiply: "))
    print(f"Product: {multiply(a, b)}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
