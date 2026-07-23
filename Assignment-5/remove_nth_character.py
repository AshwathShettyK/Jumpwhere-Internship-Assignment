# Q9: Remove Nth Character
# Remove the character at the given index from a string.

input_string = input("Enter a string: ")
index_input = input("Enter index to remove: ")

try:
    remove_index = int(index_input)
    if 0 <= remove_index < len(input_string):
        result = input_string[:remove_index] + input_string[remove_index + 1:]
    else:
        result = input_string
        print("Index out of range. String left unchanged.")
except ValueError:
    result = input_string
    print("Invalid index. Please enter an integer.")

print(f"Result: {result}")
