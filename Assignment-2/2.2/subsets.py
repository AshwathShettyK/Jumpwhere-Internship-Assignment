# Problem: Subsets
# Return all subsets of a list.

def subsets(nums):
    out = [[]]
    for n in nums:
        out += [cur + [n] for cur in out]
    return out


if __name__ == '__main__':
    nums = [1, 2, 3]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(subsets(nums))

# Time: O(2^n)
# Space: O(2^n)