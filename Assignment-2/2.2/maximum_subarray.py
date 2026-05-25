# Problem: Maximum Subarray
# Find the maximum sum of a contiguous subarray.

def max_subarray(nums):
    best = curr = nums[0]
    for n in nums[1:]:
        curr = max(n, curr + n)
        best = max(best, curr)
    return best


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(max_subarray(nums))

# Time: O(n)
# Space: O(1)