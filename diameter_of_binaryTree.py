# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 10

        def depth(node):
            if not node:
                return 0
            r = depth(node.right)
            l = depth(node.left)
            self.ans = max(r + l + 1, self.ans)
            return max(r, l) + 1

        depth(root)
        return self.ans - 1