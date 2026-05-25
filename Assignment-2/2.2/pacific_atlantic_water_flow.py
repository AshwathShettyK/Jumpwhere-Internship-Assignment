# Problem: Pacific Atlantic Water Flow
# Find cells that can reach both oceans.

from collections import deque


def pacific_atlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pacific = [[False] * cols for _ in range(rows)]
    atlantic = [[False] * cols for _ in range(rows)]
    q = deque()
    for r in range(rows):
        pacific[r][0] = True
        atlantic[r][cols - 1] = True
        q.append((r, 0, pacific))
        q.append((r, cols - 1, atlantic))
    for c in range(cols):
        pacific[0][c] = True
        atlantic[rows - 1][c] = True
        q.append((0, c, pacific))
        q.append((rows - 1, c, atlantic))

    def bfs(target):
        while q:
            r, c, vis = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not vis[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    vis[nr][nc] = True
                    q.append((nr, nc, vis))

    bfs(None)
    out = []
    for r in range(rows):
        for c in range(cols):
            if pacific[r][c] and atlantic[r][c]:
                out.append([r, c])
    return out


if __name__ == '__main__':
    heights = [[1, 2, 2, 3], [3, 2, 3, 4], [2, 4, 5, 3], [6, 7, 1, 4]]
    print('Sample Input:')
    print(heights)
    print('\nSample Output:')
    print(pacific_atlantic(heights))

# Time: O(m*n)
# Space: O(m*n)