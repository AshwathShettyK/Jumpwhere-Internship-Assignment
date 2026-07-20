# Q15: Use lambda to check whether the input is numeric.

input_value = input("Enter a value: ")

is_number = (lambda text: text.replace('.', '', 1).isdigit())(input_value)
if is_number:
    print("Valid Number")
else:
    print("Not a Number")
