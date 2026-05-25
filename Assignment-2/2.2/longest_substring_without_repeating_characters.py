# Problem: Longest Substring Without Repeating Characters
# Find the length of the longest substring with all unique chars.

def length_of_longest_substring(s):
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best


if __name__ == '__main__':
    s = 'abcabcbb'
    print('Sample Input:')
    print(s)
    print('\nSample Output:')
    print(length_of_longest_substring(s))

# Time: O(n)
# Space: O(n)