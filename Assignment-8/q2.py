# Q2: Validate parentheses using a class.

class ParenthesesValidator:
    pairs = {')': '(', '}': '{', ']': '['}

    @classmethod
    def is_valid(cls, expression):
        stack = []
        for char in expression:
            if char in '({[':
                stack.append(char)
            elif char in cls.pairs:
                if not stack or stack[-1] != cls.pairs[char]:
                    return False
                stack.pop()
        return not stack


def main():
    expression = input("Enter the expression to validate: ")
    if ParenthesesValidator.is_valid(expression):
        print("Valid expression")
    else:
        print("Invalid expression")


if __name__ == "__main__":
    main()
