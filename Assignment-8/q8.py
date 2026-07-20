# Q8: A class with methods to get and print a reversed string.

class StringHandler:
    def __init__(self):
        self.stored_string = ""

    def get_string(self, text):
        self.stored_string = text

    def print_string(self):
        reversed_text = self.stored_string[::-1]
        print(reversed_text)


def main():
    text = input("Enter a string: ")
    handler = StringHandler()
    handler.get_string(text)
    print("Reversed string:")
    handler.print_string()


if __name__ == "__main__":
    main()
