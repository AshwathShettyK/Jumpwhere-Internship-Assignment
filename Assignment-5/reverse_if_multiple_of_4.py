# Q11: Reverse If Multiple of 4
# Reverse the string only if its length is divisible by 4.

input_string = input("Enter a string: ")

if len(input_string) % 4 == 0:
    result = input_string[::-1]
else:
    result = input_string

print(f"Result: {result}")
