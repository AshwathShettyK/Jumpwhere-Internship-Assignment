# Problem: Permutations
# Return all permutations of a list.

def permutations(nums):
    out = []

    def backtrack(path, used):
        if len(path) == len(nums):
            out.append(path.copy())
            return
        for n in nums:
            if n in used:
                continue
            used.add(n)
            path.append(n)
            backtrack(path, used)
            path.pop()
            used.remove(n)

    backtrack([], set())
    return out


if __name__ == '__main__':
    nums = [1, 2, 3]
    print('Sample Input:')
    print(nums)
    print('\nSample Output:')
    print(permutations(nums))

# Time: O(n!)
# Space: O(n)