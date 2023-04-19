# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        nodes = defaultdict(int)

        def dfs(node,level):
            nonlocal total
            nodes[level] = node.val
            if nodes[level - 2] != 0 and nodes[level - 2] % 2 == 0:
                total += node.val

            if not node.left and not node.right:
                return

            if node.left:
                dfs(node.left, level + 1)

            if node.right:
                dfs(node.right, level + 1)

        dfs(root,0)

        return total