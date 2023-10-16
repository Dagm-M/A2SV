# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root
    
        def dfs(node):
            nonlocal ans
            if not node:
                return False
            
            val1 = dfs(node.left)
            val2 = dfs(node.right)
            # print(node.val, ((val1 or val2) and node.val == p.val))

            if (val1 and val2) or ((val1 or val2) and node.val == p.val) or ((val1 or val2) and node.val == q.val):
                ans = node
                return False

            if node.val == p.val or node.val == q.val:
                return True

            return val1 or val2

        dfs(root)

        return ans
