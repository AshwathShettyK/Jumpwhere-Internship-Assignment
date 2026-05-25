# Problem: Valid Parentheses
# Check if the bracket string is balanced.


def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack


if __name__ == '__main__':
    s = '([{}])'
    print('Sample Input:')
    print(s)
    print('\nSample Output:')
    print(is_valid_parentheses(s))

# Time: O(n)
# Space: O(n)