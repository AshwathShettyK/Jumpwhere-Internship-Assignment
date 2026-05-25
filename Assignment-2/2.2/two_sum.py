# Problem: Two Sum
# Find two indices whose values add to the target.

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print('Sample Input:')
    print(f'nums = {nums}')
    print(f'target = {target}')
    print('\nSample Output:')
    print(f'{two_sum(nums, target)}')

# Time: O(n)
# Space: O(n)