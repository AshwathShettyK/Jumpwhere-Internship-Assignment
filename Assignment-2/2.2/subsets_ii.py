# Problem: Subsets II
# Return all unique subsets with duplicates.

def subsets_with_dup(nums):
    nums.sort()
    out = [[]]
    for i, n in enumerate(nums):
        if i and n == nums[i - 1]:
            out += [cur + [n] for cur in out[-len(out) // 2:]]
        else:
            out += [cur + [n] for cur in out]
    return out


if __name__ == '__main__':
    nums = [1, 2, 2]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(subsets_with_dup(nums))

# Time: O(2^n)
# Space: O(2^n)