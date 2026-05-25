# Problem: Validate Binary Search Tree
# Check whether a binary tree is a valid BST.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    def dfs(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    return dfs(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print('Sample Input:')
    print('2 /\\ 1 3')
    print('\nSample Output:')
    print(is_valid_bst(root))

# Time: O(n)
# Space: O(h)