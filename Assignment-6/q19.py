# Q19: Separate a mixed list into integers, strings, and floats.

mixed_input = input("Enter mixed items separated by spaces: ")
input_items = mixed_input.split()

integers = []
strings = []
floats = []

for item in input_items:
    try:
        integer_value = int(item)
        integers.append(integer_value)
        continue
    except ValueError:
        pass

    try:
        float_value = float(item)
        floats.append(float_value)
        continue
    except ValueError:
        pass

    strings.append(item)

print("Integers:", integers)
print("Strings:", strings)
print("Floats:", floats)
