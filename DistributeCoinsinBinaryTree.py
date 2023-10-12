# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(root):
            if not root:
                return 0

            right = dfs(root.right)
            left = dfs(root.left)

            excess = root.val -1 + left + right
            self.moves += abs(excess)

            return excess

        dfs(root)

        return self.moves
