# Problem: Number of Islands
# Count islands of land in a grid.

def num_islands(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count


if __name__ == '__main__':
    grid = [
        ['1', '1', '0', '0'],
        ['1', '1', '0', '0'],
        ['0', '0', '1', '0'],
        ['0', '0', '0', '1']
    ]
    print('Sample Input:')
    print(grid)
    print('\nSample Output:')
    print(num_islands(grid))

# Time: O(m*n)
# Space: O(m*n)