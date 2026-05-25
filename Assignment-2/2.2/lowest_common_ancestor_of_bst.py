# Problem: Lowest Common Ancestor of BST
# Find the LCA of two nodes in a BST.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None


if __name__ == '__main__':
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    p = root.left
    q = root.left.right
    print('Sample Input:')
    print('p = 2, q = 4')
    print('\nSample Output:')
    print(lowest_common_ancestor(root, p, q).val)

# Time: O(h)
# Space: O(1)