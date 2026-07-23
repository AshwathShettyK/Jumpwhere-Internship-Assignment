# Q14: Print multiplication tables for 24, 50, and 29 from 1 to 10.

numbers_to_print = [24, 50, 29]
for number in numbers_to_print:
    print(f"Multiplication table for {number}:")
    for multiplier in range(1, 11):
        product = number * multiplier
        print(f"{number} x {multiplier} = {product}")
    print()
