# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        seen = defaultdict(int)

        if root == None:
            return 0

        def dfs(node,currSum):
            nonlocal ans
            currSum += node.val
            if not node.left and not node.right:
                if (currSum - targetSum) in seen:
                    ans += seen[(currSum - targetSum)]
                if currSum == targetSum:
                    ans += 1
                return

            if (currSum - targetSum) in seen:
                ans += seen[(currSum - targetSum)]
            if currSum == targetSum:
                ans += 1

            seen[currSum] += 1
            if node.left:
                dfs(node.left, currSum)
            
            if node.right:
                dfs(node.right, currSum)

            seen[currSum] -= 1
            if seen[currSum] == 0:
                del seen[currSum]

        dfs(root, 0)

        return ans
