# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self,root):
        if root == None:
            return []

        ans = []

        ans.extend(self.inOrder(root.left))
        ans.append(root.val)
        ans.extend(self.inOrder(root.right))

        return ans

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = self.inOrder(root)
        sort = sorted(arr)
        s = set(arr)

        if len(s) != len(arr):
            return False
        
        if sort != arr:
            return False

        return True
