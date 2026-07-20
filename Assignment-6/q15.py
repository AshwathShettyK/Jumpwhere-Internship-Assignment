# Q15: Continue taking integers until the user chooses to quit.

numbers = []
while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    numbers.append(number)
    choice = input("Press q to quit or any other key to continue: ")
    if choice.lower() == 'q':
        break

if numbers:
    average = sum(numbers) / len(numbers)
    product = 1
    for value in numbers:
        product *= value

    print(f"Average of entered numbers: {average}")
    print(f"Product of entered numbers: {product}")
else:
    print("No numbers were entered.")
