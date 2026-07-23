# Q5: Swap First Two Characters
# Accept two strings and swap their first two characters.

first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

if len(first_string) >= 2:
    first_prefix = first_string[:2]
    first_rest = first_string[2:]
else:
    first_prefix = first_string
    first_rest = ""

if len(second_string) >= 2:
    second_prefix = second_string[:2]
    second_rest = second_string[2:]
else:
    second_prefix = second_string
    second_rest = ""

new_first = second_prefix + first_rest
new_second = first_prefix + second_rest

print("Result:", new_first, new_second)
