# Q4: Find two numbers whose sum equals the target using a class.

class TwoSumFinder:
    @staticmethod
    def find_indices(numbers, target):
        lookup = {}
        for index, value in enumerate(numbers):
            complement = target - value
            if complement in lookup:
                return lookup[complement], index
            lookup[value] = index
        return None


def main():
    try:
        numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
        target = int(input("Enter the target value: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    result = TwoSumFinder.find_indices(numbers, target)
    if result:
        print(f"Indices of numbers with sum {target}: {result}")
    else:
        print("No two numbers add up to the target.")


if __name__ == "__main__":
    main()
