# Problem: House Robber
# Maximize stolen money without robbing adjacent houses.

def rob(nums):
    prev2 = 0
    prev1 = 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(rob(nums))

# Time: O(n)
# Space: O(1)