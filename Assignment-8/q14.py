# Q14: Use lambda to check if a string starts with a given character.

input_string = input("Enter a string: ")
start_char = input("Enter the starting character: ")

starts_with = (lambda text, char: text.startswith(char))(input_string, start_char)
print(f"Starts with '{start_char}': {starts_with}")
