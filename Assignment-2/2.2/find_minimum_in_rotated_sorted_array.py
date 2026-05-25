# Problem: Find Minimum in Rotated Sorted Array
# Find the smallest value in a rotated sorted array.

def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(find_min(nums))

# Time: O(log n)
# Space: O(1)