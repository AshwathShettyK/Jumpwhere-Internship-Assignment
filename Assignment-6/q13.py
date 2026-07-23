# Q13: Take 10 integers and print their average.

numbers = []
for count in range(1, 11):
    user_input = input(f"Enter integer {count}: ")
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        raise SystemExit
    numbers.append(number)

average = sum(numbers) / len(numbers)
print(f"Average of the entered numbers: {average}")
