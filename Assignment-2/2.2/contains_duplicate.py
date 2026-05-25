# Problem: Contains Duplicate
# Return True if any number appears more than once.

def contains_duplicate(nums):
    return len(nums) != len(set(nums))


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print('Sample Input:')
    print(f'nums = {nums}')
    print('\nSample Output:')
    print(contains_duplicate(nums))

# Time: O(n)
# Space: O(n)