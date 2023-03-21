# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        seen = defaultdict(int)
        sum_ = 0
        curr = 0

        def path(root):
            nonlocal curr, sum_
            curr += root.val
            sum_ += seen[curr - targetSum]
            
            seen[curr] += 1
            if curr == targetSum:
                sum_ += 1
            

            if not root.left and not root.right:
                return

            if root.left:
                path(root.left)
                seen[curr] -= 1
                curr -= root.left.val

            if root.right:
                path(root.right)
                seen[curr] -= 1
                curr -= root.right.val

        path(root)

        return sum_
