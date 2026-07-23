# Q6: Implement pow(x, n) without using built-in pow().

class PowerCalculator:
    @staticmethod
    def power(base, exponent):
        result = 1
        is_negative_exponent = exponent < 0
        exponent = abs(exponent)

        for _ in range(exponent):
            result *= base

        if is_negative_exponent:
            if result == 0:
                raise ZeroDivisionError("Cannot raise 0 to a negative power")
            result = 1 / result

        return result


def main():
    try:
        base = float(input("Enter the base: "))
        exponent = int(input("Enter the exponent: "))
    except ValueError:
        print("Invalid input. Please enter a number and an integer.")
        return

    try:
        print(f"Result: {PowerCalculator.power(base, exponent)}")
    except ZeroDivisionError as error:
        print(error)


if __name__ == "__main__":
    main()
