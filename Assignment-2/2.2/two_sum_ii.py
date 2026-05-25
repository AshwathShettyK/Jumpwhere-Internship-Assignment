# Problem: Two Sum II
# Find two indices in a sorted array that sum to target.

def two_sum_ii(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left + 1, right + 1]
        if s < target:
            left += 1
        else:
            right -= 1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print('Sample Input:')
    print(f'nums = {nums}')
    print(f'target = {target}')
    print('\nSample Output:')
    print(two_sum_ii(nums, target))

# Time: O(n)
# Space: O(1)