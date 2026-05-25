# Problem: Subtree of Another Tree
# Check whether one tree is a subtree of another.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if not root:
        return '#'
    return f'{root.val},{serialize(root.left)},{serialize(root.right)}'


def is_subtree(root, sub):
    return serialize(sub) in serialize(root)


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    print('Sample Input:')
    print('root contains subtree')
    print('\nSample Output:')
    print(is_subtree(root, sub))

# Time: O(n*m)
# Space: O(n+m)