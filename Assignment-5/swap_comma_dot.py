# Q18: Swap Comma and Dot
# Swap commas and dots in the string.

input_string = input("Enter a string with commas and dots: ")

# Replace commas with a temporary marker, replace dots with commas, then replace marker with dots.
temp_string = input_string.replace(",", "<COMMA>")
temp_string = temp_string.replace(".", ",")
result = temp_string.replace("<COMMA>", ".")

print(f"Swapped string: {result}")
