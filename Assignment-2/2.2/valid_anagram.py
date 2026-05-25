# Problem: Valid Anagram
# Check whether two strings are anagrams.

from collections import Counter


def valid_anagram(a, b):
    return Counter(a) == Counter(b)


if __name__ == '__main__':
    a = 'listen'
    b = 'silent'
    print('Sample Input:')
    print(f'a = {a}')
    print(f'b = {b}')
    print('\nSample Output:')
    print(valid_anagram(a, b))

# Time: O(n)
# Space: O(k)