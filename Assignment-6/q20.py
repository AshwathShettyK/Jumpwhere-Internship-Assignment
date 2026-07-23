# Q20: Create a list of squared values from a list of integers.

input_values = input("Enter integer values separated by spaces: ")
number_strings = input_values.split()

original_numbers = []
squared_numbers = []

for value in number_strings:
    try:
        number = int(value)
    except ValueError:
        print(f"Skipping invalid input: {value}")
        continue

    original_numbers.append(number)
    squared_numbers.append(number ** 2)

print("Original list:", original_numbers)
print("Squared list:", squared_numbers)
