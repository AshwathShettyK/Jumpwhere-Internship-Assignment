# Q6: Add 'ing' or 'ly'
# Modify the string based on its current ending.

input_string = input("Enter a string: ")

if len(input_string) < 3:
    result = input_string  # Leave strings shorter than 3 unchanged
elif input_string.endswith("ing"):
    result = input_string + "ly"
else:
    result = input_string + "ing"

print(f"Modified string: {result}")
