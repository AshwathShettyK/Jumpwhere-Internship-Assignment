# Problem: Permutation in String
# Check if s2 contains a permutation of s1.

from collections import Counter


def check_inclusion(s1, s2):
    need = Counter(s1)
    window = Counter()
    left = 0
    for right, ch in enumerate(s2):
        window[ch] += 1
        if right - left + 1 > len(s1):
            left_ch = s2[left]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]
            left += 1
        if window == need:
            return True
    return False


if __name__ == '__main__':
    s1 = 'ab'
    s2 = 'eidbaooo'
    print('Sample Input:')
    print(f's1 = {s1}')
    print(f's2 = {s2}')
    print('\nSample Output:')
    print(check_inclusion(s1, s2))

# Time: O(n)
# Space: O(k)