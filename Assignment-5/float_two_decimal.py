# Q14: Float Two Decimal Places
# Print the floating-point number up to two decimal places.

input_value = input("Enter a floating-point number: ")

try:
    number = float(input_value)
    result = f"{number:.2f}"
    print(f"Formatted number: {result}")
except ValueError:
    print("Invalid input. Please enter a valid floating-point number.")
