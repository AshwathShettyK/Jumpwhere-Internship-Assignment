# Balanced Delimiters Checker
# Reads a string from the user and prints True if delimiters are balanced.


def is_balanced(expression):
    """Check if the delimiters in the expression are balanced."""
    # Mapping for closing brackets to their matching opening brackets
    bracket_pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    # Stack to keep opening brackets
    stack = []

    for char in expression:
        if char in bracket_pairs.values():
            # Push opening bracket onto the stack
            stack.append(char)
        elif char in bracket_pairs:
            # If stack is empty or top does not match, expression is not balanced
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
        else:
            # Ignore non-bracket characters
            continue

    # Expression is balanced when no unmatched opening brackets remain
    return len(stack) == 0


def main():
    expression = input("Enter a string: ")
    result = is_balanced(expression)
    print(result)


if __name__ == "__main__":
    main()
