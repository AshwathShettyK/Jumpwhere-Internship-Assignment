# Hangman Game
# Reads words from words.txt and plays a console-based Hangman game.

import random
from pathlib import Path


def load_words():
    """Load words from words.txt and return them as a list."""
    words_file = Path(__file__).resolve().parent / "words.txt"
    words = []
    with open(words_file, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip().upper()
            if word:
                words.append(word)
    return words


def choose_word(words_list):
    """Select a random word from the list."""
    return random.choice(words_list)


def display_word(secret_word, guessed_letters):
    """Return the current word display with underscores for hidden letters."""
    displayed = [letter if letter in guessed_letters else "_" for letter in secret_word]
    return " ".join(displayed)


def get_valid_letter(guessed_letters):
    """Get a single valid letter from the user."""
    while True:
        guess = input("Guess a letter: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single alphabet character.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            print("Try another one.")
            continue
        return guess


def play_game(words_list):
    """Play one round of Hangman."""
    secret_word = choose_word(words_list)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman!\n")
    while True:
        print(display_word(secret_word, guessed_letters))
        print("\nGuessed Letters:")
        print(" ".join(sorted(guessed_letters)))

        guess = get_valid_letter(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct!\n")
        else:
            wrong_guesses += 1
            print("Incorrect!")
            print(f"You have {max_wrong - wrong_guesses} guesses left.\n")

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations!\n")
            print("You guessed the word correctly!\n")
            print("Word:")
            print(secret_word)
            break

        if wrong_guesses >= max_wrong:
            print("Game Over!\n")
            print("The correct word was:\n")
            print(secret_word)
            break


def play_again():
    """Ask the user whether they want to play again."""
    while True:
        answer = input("Do you want to play again? (Y/N) ").strip().upper()
        if answer == "Y":
            return True
        if answer == "N":
            return False
        print("Invalid input. Please enter Y or N.")


def main():
    words_list = load_words()
    if not words_list:
        print("No words found in words.txt.")
        return

    while True:
        play_game(words_list)
        if not play_again():
            break
    print("Thank you for playing Hangman!")


if __name__ == "__main__":
    main()
