# Problem: Combination Sum
# Return all combinations that sum to target.

def combination_sum(candidates, target):
    out = []

    def dfs(i, rem, path):
        if rem == 0:
            out.append(path.copy())
            return
        if rem < 0:
            return
        for j in range(i, len(candidates)):
            path.append(candidates[j])
            dfs(j, rem - candidates[j], path)
            path.pop()

    dfs(0, target, [])
    return out


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print('Sample Input:')
    print(f'candidates = {candidates}')
    print(f'target = {target}')
    print('\nSample Output:')
    print(combination_sum(candidates, target))

# Time: O(2^n)
# Space: O(n)