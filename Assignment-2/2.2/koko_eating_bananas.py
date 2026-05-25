# Problem: Koko Eating Bananas
# Find the minimum eating speed so Koko finishes in h hours.

def min_speed(piles, h):
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        hours = sum((p + mid - 1) // mid for p in piles)
        if hours <= h:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    print('Sample Input:')
    print(f'piles = {piles}')
    print(f'h = {h}')
    print('\nSample Output:')
    print(min_speed(piles, h))

# Time: O(n log max(piles))
# Space: O(1)