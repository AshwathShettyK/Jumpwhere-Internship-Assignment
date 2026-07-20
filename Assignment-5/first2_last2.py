# Q3: First Two and Last Two Characters
# Return the first two and last two characters of a string.

input_string = input("Enter a string: ")

if len(input_string) < 2:
    result = ""
else:
    result = input_string[:2] + input_string[-2:]

print(f"Result: {result}")
