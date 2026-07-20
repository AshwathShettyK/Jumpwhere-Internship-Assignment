# Q10: Display the class name of an object instance.

class ExampleClass:
    def __init__(self):
        self.message = "Hello"


def main():
    example = ExampleClass()
    print("Class name of the object instance:", example.__class__.__name__)


if __name__ == "__main__":
    main()
