# Q4: Replace First Character
# Replace all occurrences of the first character with '$' except for the first occurrence.

input_string = input("Enter a string: ")

if input_string:
    first_char = input_string[0]
    remainder = input_string[1:]
    replaced_remainder = remainder.replace(first_char, "$")
    result = first_char + replaced_remainder
else:
    result = ""

print(f"Modified string: {result}")
