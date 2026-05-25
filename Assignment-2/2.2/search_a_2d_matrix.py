# Problem: Search a 2D Matrix
# Search a target in a sorted matrix.

def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target:
            return True
        if val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print('Sample Input:')
    print(matrix)
    print(f'target = {target}')
    print('\nSample Output:')
    print(search_matrix(matrix, target))

# Time: O(log(m*n))
# Space: O(1)