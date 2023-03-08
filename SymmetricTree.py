# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self,p,q):
        if q == None or p == None:
            if q == None and p == None:
                return True
            else:
                return False

        if p.val != q.val:
            return False

        left = self.isSameTree(p.left,q.right)
        right = self.isSameTree(p.right,q.left)

        return left and right

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        return self.isSameTree(root.left,root.right)
