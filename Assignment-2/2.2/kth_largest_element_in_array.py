# Problem: Kth Largest Element in Array
# Return the kth largest element.

import heapq


def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print('Sample Input:')
    print(f'nums = {nums}')
    print(f'k = {k}')
    print('\nSample Output:')
    print(find_kth_largest(nums, k))

# Time: O(n log k)
# Space: O(k)