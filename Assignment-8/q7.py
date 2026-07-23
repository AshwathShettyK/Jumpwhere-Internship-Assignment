# Q7: Reverse a string word by word using a class.

class WordReverser:
    @staticmethod
    def reverse_words(text):
        words = text.split()
        return " ".join(reversed(words))


def main():
    text = input("Enter a string: ")
    reversed_text = WordReverser.reverse_words(text)
    print("Reversed string:")
    print(reversed_text)


if __name__ == "__main__":
    main()
