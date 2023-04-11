"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        max_level = 1

        def dfs(node,level):
            nonlocal max_level

            if len(node.children) == 0:
                max_level = max(max_level,level)
                return

            for c in node.children:
                dfs(c,level+1)

        dfs(root,1)

        return max_level