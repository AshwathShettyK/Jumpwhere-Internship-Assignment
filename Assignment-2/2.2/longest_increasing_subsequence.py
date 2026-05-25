from bisect import bisect_left

# Problem: Longest Increasing Subsequence
# Find the length of the LIS.

def length_of_lis(nums):
    tails = []
    for n in nums:
        i = bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(length_of_lis(nums))

# Time: O(n log n)
# Space: O(n)