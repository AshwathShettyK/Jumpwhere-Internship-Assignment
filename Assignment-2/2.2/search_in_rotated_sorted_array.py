# Problem: Search in Rotated Sorted Array
# Search for target in a rotated sorted array.

def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print('Sample Input:')
    print(f'nums = {nums}')
    print(f'target = {target}')
    print('\nSample Output:')
    print(search_rotated(nums, target))

# Time: O(log n)
# Space: O(1)