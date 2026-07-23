# Q3: Generate all unique subsets of a list of distinct integers.

class SubsetGenerator:
    @staticmethod
    def generate_subsets(numbers):
        subsets = [[]]
        for number in numbers:
            subsets += [current + [number] for current in subsets]
        return subsets


def main():
    input_string = input("Enter distinct integers separated by spaces: ")
    try:
        numbers = [int(value) for value in input_string.split()]
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    subsets = SubsetGenerator.generate_subsets(numbers)
    print("Generated subsets:")
    for subset in subsets:
        print(subset)


if __name__ == "__main__":
    main()
