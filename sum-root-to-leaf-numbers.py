# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(node,num):
            nonlocal total
            num.append(str(node.val))

            if not node.left and not node.right:
                total += int("".join(num))

            
            if node.left:
                dfs(node.left,num)
                num.pop()

            if node.right:
                dfs(node.right,num)
                num.pop()

        dfs(root,[])

        return total