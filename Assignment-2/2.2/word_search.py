# Problem: Word Search
# Check if a word exists in the board by moving in 4 directions.

def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False
        ch = board[r][c]
        board[r][c] = '#'
        ok = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
        board[r][c] = ch
        return ok

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = 'ABCCED'
    print('Sample Input:')
    print(board)
    print(f'word = {word}')
    print('\nSample Output:')
    print(exist(board, word))

# Time: O(m*n*4^L)
# Space: O(L)