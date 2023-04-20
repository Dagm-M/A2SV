# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = -inf

        def dfs(node):
            nonlocal total
            if not node.left and not node.right:
                total = max(total,node.val)
                return node.val

            if node.left:
                left = dfs(node.left)

            if node.right:
                right = dfs(node.right)

            temp = 0
            if node.left and node.right:
                
                temp = max(left + node.val, node.val)
                temp = max(right + temp, temp)
                total = max(total,temp)
                    
                if left > right:
                    temp = max(left + node.val, node.val)
                else:
                    temp = max(right + node.val, node.val)
            elif node.left:
                temp = max(left + node.val, node.val)
               
            else:
                temp = max(right + node.val, node.val)
                
            total = max(total, temp)

            return temp

        dfs(root)

        return total