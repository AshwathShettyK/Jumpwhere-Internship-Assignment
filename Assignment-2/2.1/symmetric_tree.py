from collections import deque


class TreeNode:
    def __init__(self, v=0, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r


def is_symmetric(root):
    if not root:
        return True
    q = deque([(root.left, root.right)])
    while q:
        a, b = q.popleft()
        if not a and not b:
            continue
        if not a or not b or a.val != b.val:
            return False
        q.append((a.left, b.right))
        q.append((a.right, b.left))
    return True


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print("Sample Input:")
    print("Binary tree is symmetric.")
    print("\nSample Output:")
    print(f"Is the tree symmetric? {is_symmetric(root)}")
