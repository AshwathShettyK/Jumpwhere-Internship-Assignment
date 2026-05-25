# Problem: Product of Array Except Self
# Compute prefix/suffix products without division.

def product_except_self(nums):
    n = len(nums)
    ans = [1] * n
    for i in range(1, n):
        ans[i] = ans[i - 1] * nums[i - 1]
    right = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]
    return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print('Sample Input:')
    print(f'nums = {nums}')
    print('\nSample Output:')
    print(product_except_self(nums))

# Time: O(n)
# Space: O(n)