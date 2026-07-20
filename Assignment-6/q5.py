# Q5: Calculate sum and average of integers until the user enters 0.

total_sum = 0
count = 0

while True:
    user_input = input("Enter an integer (0 to stop): ")
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if number == 0:
        break

    total_sum += number
    count += 1

if count == 0:
    print("No numbers were entered.")
else:
    average = total_sum / count
    print(f"Sum of entered numbers: {total_sum}")
    print(f"Average of entered numbers: {average}")
