# Q20: Remove Consecutive Duplicates
# Remove consecutive duplicate characters from a string.

input_string = input("Enter a string: ")

if input_string:
    result_chars = [input_string[0]]
    for character in input_string[1:]:
        if character != result_chars[-1]:
            result_chars.append(character)
    result = "".join(result_chars)
else:
    result = ""

print(f"Result: {result}")
