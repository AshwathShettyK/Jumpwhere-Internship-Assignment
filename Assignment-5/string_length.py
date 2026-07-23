# Q1: String Length
# Calculate the length of a string without using len().

input_string = input("Enter a string: ")

character_count = 0
for character in input_string:
    character_count += 1  # Count each character manually

print(f"The length of the string is: {character_count}")
