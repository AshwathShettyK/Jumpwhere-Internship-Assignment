# Q7: Replace 'not'...'poor' with 'good'
# If 'poor' comes after 'not', replace the substring from 'not' to 'poor' with 'good'.

input_string = input("Enter a sentence: ")

not_index = input_string.find("not")
poor_index = input_string.find("poor")

if not_index != -1 and poor_index != -1 and poor_index > not_index:
    result = input_string[:not_index] + "good" + input_string[poor_index + 4:]
else:
    result = input_string

print(f"Result: {result}")
