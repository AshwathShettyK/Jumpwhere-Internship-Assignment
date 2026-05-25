# Problem: Jump Game
# Check whether you can reach the last index.

def can_jump(nums):
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + n)
    return True


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(can_jump(nums))

# Time: O(n)
# Space: O(1)