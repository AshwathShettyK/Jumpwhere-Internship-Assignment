# Problem: Binary Search
# Search for a target in a sorted array.

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print('Sample Input:')
    print(f'nums = {nums}')
    print(f'target = {target}')
    print('\nSample Output:')
    print(binary_search(nums, target))

# Time: O(log n)
# Space: O(1)