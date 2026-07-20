# Cows and Bulls Game
# Generates a 4-digit secret number with unique digits and lets the user guess it.

import random


def generate_secret_number():
    """Generate a 4-digit number with unique digits and no leading zero."""
    first_digit = random.choice('123456789')
    remaining_digits = list(set('0123456789') - {first_digit})
    secret_digits = [first_digit] + random.sample(remaining_digits, 3)
    return "".join(secret_digits)


def is_valid_guess(guess):
    """Check whether the guess is a valid 4-digit number with unique digits."""
    if not guess.isdigit():
        print("Invalid input. Please enter digits only.")
        return False
    if len(guess) != 4:
        print("Invalid input. Please enter exactly 4 digits.")
        return False
    if len(set(guess)) != 4:
        print("Invalid input. Digits must not repeat.")
        return False
    return True


def calculate_cows_bulls(secret_number, guess):
    """Return the number of cows and bulls for a guess."""
    cows = sum(1 for i in range(4) if guess[i] == secret_number[i])
    bulls = sum(1 for char in guess if char in secret_number) - cows
    return cows, bulls


def play_game():
    """Play the Cows and Bulls game until the user guesses correctly."""
    secret_number = generate_secret_number()
    guess_count = 0

    print("Welcome to the Cows and Bulls Game!\n")
    while True:
        guess = input("Guess the 4-digit number: ")
        if not is_valid_guess(guess):
            continue

        guess_count += 1
        cows, bulls = calculate_cows_bulls(secret_number, guess)

        if cows == 4:
            print("\nCongratulations!\n")
            print("You guessed the correct number.\n")
            print(f"Secret Number : {secret_number}\n")
            print(f"Total Guesses : {guess_count}")
            break

        print(f"{cows} Cow{'s' if cows != 1 else ''}")
        print(f"{bulls} Bull{'s' if bulls != 1 else ''}\n")


if __name__ == "__main__":
    play_game()
