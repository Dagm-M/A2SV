# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return root

        if root.val == val:
            return root

        ans = None
        if val > root.val:
            ans = self.searchBST(root.right,val)
        else:
            ans = self.searchBST(root.left,val)

        return ans
