# Problem: Hand of Straights
# Check whether cards can be grouped into consecutive hands.

from collections import Counter


def is_n_straight_hand(hand, group_size):
    counts = Counter(hand)
    for card in sorted(counts):
        if counts[card] > 0:
            for x in range(card, card + group_size):
                if counts[x] == 0:
                    return False
                counts[x] -= 1
    return True


if __name__ == '__main__':
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    group_size = 3
    print('Sample Input:')
    print(f'hand = {hand}')
    print(f'group_size = {group_size}')
    print('\nSample Output:')
    print(is_n_straight_hand(hand, group_size))

# Time: O(n log n)
# Space: O(n)