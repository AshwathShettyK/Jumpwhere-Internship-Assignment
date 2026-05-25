# Problem: House Robber II
# Maximize robbed money in a circular arrangement.

def rob(nums):
    if len(nums) == 1:
        return nums[0]
    def solve(a):
        prev2 = prev1 = 0
        for n in a:
            prev2, prev1 = prev1, max(prev1, prev2 + n)
        return prev1
    return max(solve(nums[:-1]), solve(nums[1:]))


if __name__ == '__main__':
    nums = [2, 3, 2]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(rob(nums))

# Time: O(n)
# Space: O(1)