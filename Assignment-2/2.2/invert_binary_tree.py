# Problem: Invert Binary Tree
# Swap left and right children recursively.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if not root:
        return root
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    root = invert_tree(root)
    print('Sample Input:')
    print('4 /\\ 7 2')
    print('\nSample Output:')
    print(root.left.val, root.right.val)

# Time: O(n)
# Space: O(h)