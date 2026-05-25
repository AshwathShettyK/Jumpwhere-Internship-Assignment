# Problem: Longest Repeating Character Replacement
# Replace at most k chars to make the substring uniform.

def character_replacement(s, k):
    counts = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        while right - left + 1 - max(counts.values()) > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == '__main__':
    s = 'ABAB'
    k = 2
    print('Sample Input:')
    print(f's = {s}')
    print(f'k = {k}')
    print('\nSample Output:')
    print(character_replacement(s, k))

# Time: O(n)
# Space: O(26)