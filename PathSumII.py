# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if root == None:
            return []

        def dfs(node, path, currSum):
            if not node.left and not node.right:
                path.append(node.val)
                if currSum + node.val == targetSum:
                    ans.append(path.copy())
                path.pop()
                return

            path.append(node.val)
            if node.left:
                dfs(node.left, path, currSum + node.val)
            
            if node.right:
                dfs(node.right, path, currSum + node.val)

            path.pop()

        dfs(root, [], 0)

        return ans
