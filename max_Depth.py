
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def depth(node):
            d = 1
            if not node: return 0
            if not node.children: return 1
            for child in node.children:
                d = max(depth(child) + 1, d)
            return d

        return depth(root)