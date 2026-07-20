# Q7: Count how many elements of a list are greater than 30.

input_values = input("Enter numbers separated by spaces: ")
number_strings = input_values.split()

numbers = []
for value in number_strings:
    try:
        numbers.append(float(value))
    except ValueError:
        print(f"Skipping invalid input: {value}")

count_above_30 = 0
for number in numbers:
    if number > 30:
        count_above_30 += 1

print(f"Count of numbers greater than 30: {count_above_30}")
