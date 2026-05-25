# Problem: Group Anagrams
# Group words that are anagrams of each other.

from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups[tuple(sorted(w))].append(w)
    return list(groups.values())


if __name__ == '__main__':
    words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print('Sample Input:')
    print(words)
    print('\nSample Output:')
    print(group_anagrams(words))

# Time: O(n * k log k)
# Space: O(n * k)