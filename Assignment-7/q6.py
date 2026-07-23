# Q6: Generate a dictionary of numbers from 1 to n with square values.

try:
    n = int(input("Enter the value of n: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    raise SystemExit

if n < 1:
    print("Enter a number greater than 0.")
    raise SystemExit

result_dict = {number: number * number for number in range(1, n + 1)}
print("Generated dictionary:")
print(result_dict)
