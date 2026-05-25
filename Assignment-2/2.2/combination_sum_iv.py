# Problem: Combination Sum IV
# Count the number of ordered combinations that sum to target.

def combination_sum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for x in range(1, target + 1):
        for n in nums:
            if x >= n:
                dp[x] += dp[x - n]
    return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print('Sample Input:')
    print(f'nums = {nums}')
    print(f'target = {target}')
    print('\nSample Output:')
    print(combination_sum4(nums, target))

# Time: O(target * len(nums))
# Space: O(target)