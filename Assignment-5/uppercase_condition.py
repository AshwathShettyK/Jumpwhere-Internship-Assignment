# Q12: Uppercase Condition
# Convert the string to uppercase only if at least two uppercase letters occur in the first four characters.

input_string = input("Enter a string: ")

first_four = input_string[:4]
uppercase_count = 0
for character in first_four:
    if character.isupper():
        uppercase_count += 1

if uppercase_count >= 2:
    result = input_string.upper()
else:
    result = input_string

print(f"Result: {result}")
