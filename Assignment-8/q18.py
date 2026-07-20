# Q18: Validate a string using lambda for uppercase, lowercase, digit, and length.

input_string = input("Enter a string: ")

has_upper = any(map(lambda c: c.isupper(), input_string))
has_lower = any(map(lambda c: c.islower(), input_string))
has_digit = any(map(lambda c: c.isdigit(), input_string))
is_long_enough = len(input_string) >= 10

if has_upper and has_lower and has_digit and is_long_enough:
    print("Valid String")
else:
    print("Invalid String")
