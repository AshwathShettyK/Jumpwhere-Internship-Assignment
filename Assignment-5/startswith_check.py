# Q13: Startswith Check
# Check whether a string starts with the user-specified prefix.

input_string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")

starts_with_prefix = input_string.startswith(prefix)
print(f"Does the string start with '{prefix}'? {starts_with_prefix}")
