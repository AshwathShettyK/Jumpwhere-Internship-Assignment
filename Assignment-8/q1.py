# Q1: Convert integer to Roman numeral and Roman numeral to integer using a class.

class RomanConverter:
    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    @classmethod
    def integer_to_roman(cls, number):
        result = ""
        for value, numeral in cls.roman_map:
            while number >= value:
                result += numeral
                number -= value
        return result

    @classmethod
    def roman_to_integer(cls, roman_string):
        roman_values = {numeral: value for value, numeral in cls.roman_map}
        i = 0
        result = 0
        while i < len(roman_string):
            if i + 1 < len(roman_string) and roman_string[i:i + 2] in roman_values:
                result += roman_values[roman_string[i:i + 2]]
                i += 2
            else:
                result += roman_values[roman_string[i]]
                i += 1
        return result


def main():
    print("1. Integer to Roman")
    print("2. Roman to Integer")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        try:
            number = int(input("Enter an integer: "))
            if number <= 0:
                print("Enter a positive integer.")
                return
            print("Roman numeral:", RomanConverter.integer_to_roman(number))
        except ValueError:
            print("Invalid integer input.")
    elif choice == "2":
        roman_input = input("Enter a Roman numeral: ").upper().strip()
        try:
            print("Integer value:", RomanConverter.roman_to_integer(roman_input))
        except KeyError:
            print("Invalid Roman numeral.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
