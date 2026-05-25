# Problem: Single Number
# Find the element that appears once while others appear twice.

def single_number(nums):
    x = 0
    for n in nums:
        x ^= n
    return x


if __name__ == '__main__':
    nums = [2, 2, 1]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(single_number(nums))

# Time: O(n)
# Space: O(1)