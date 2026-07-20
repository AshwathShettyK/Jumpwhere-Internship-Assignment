# Q16: Character Index
# Print every character along with its index in the string.

input_string = input("Enter a string: ")

for index, character in enumerate(input_string):
    print(f"Index {index}: {character}")
