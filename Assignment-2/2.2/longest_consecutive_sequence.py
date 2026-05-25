# Problem: Longest Consecutive Sequence
# Find the length of the longest consecutive sequence.

def longest_consecutive(nums):
    s = set(nums)
    best = 0
    for n in s:
        if n - 1 not in s:
            length = 0
            while n + length in s:
                length += 1
            best = max(best, length)
    return best


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(longest_consecutive(nums))

# Time: O(n)
# Space: O(n)