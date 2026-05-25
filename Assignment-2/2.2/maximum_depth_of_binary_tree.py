# Problem: Maximum Depth of Binary Tree
# Return the height of the binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print('Sample Input:')
    print('3, 9, 20, 15, 7')
    print('\nSample Output:')
    print(max_depth(root))

# Time: O(n)
# Space: O(h)