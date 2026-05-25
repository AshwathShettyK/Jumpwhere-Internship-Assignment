# Problem: 3Sum
# Return all triplets summing to zero.

def three_sum(nums):
    nums.sort()
    out = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                out.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return out


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(three_sum(nums))

# Time: O(n^2)
# Space: O(1)