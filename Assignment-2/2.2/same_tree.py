# Problem: Same Tree
# Check whether two binary trees are structurally the same.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def same_tree(a, b):
    if not a and not b:
        return True
    if not a or not b or a.val != b.val:
        return False
    return same_tree(a.left, b.left) and same_tree(a.right, b.right)


if __name__ == '__main__':
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    b = TreeNode(1, TreeNode(2), TreeNode(3))
    print('Sample Input:')
    print('Tree A and Tree B are identical')
    print('\nSample Output:')
    print(same_tree(a, b))

# Time: O(n)
# Space: O(h)