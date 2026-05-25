# Problem: Valid Palindrome
# Check whether the string is a palindrome ignoring non-alphanumerics.

def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == '__main__':
    s = 'A man, a plan, a canal: Panama'
    print('Sample Input:')
    print(s)
    print('\nSample Output:')
    print(is_palindrome(s))

# Time: O(n)
# Space: O(n)