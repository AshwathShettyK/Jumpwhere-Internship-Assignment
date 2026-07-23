# Q5: Find all triplets whose sum is zero using a class.

class ThreeSumFinder:
    @staticmethod
    def find_triplets(numbers):
        numbers.sort()
        triplets = []
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, len(numbers) - 1
            while left < right:
                total = numbers[i] + numbers[left] + numbers[right]
                if total == 0:
                    triplets.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return triplets


def main():
    try:
        numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    triplets = ThreeSumFinder.find_triplets(numbers)
    if triplets:
        print("Triplets with sum zero:")
        for triplet in triplets:
            print(triplet)
    else:
        print("No triplets found with sum zero.")


if __name__ == "__main__":
    main()
