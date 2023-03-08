# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None and root2 == None:
            return None
        
        newNode = TreeNode()

        if root1 != None and root2 != None:
            newNode.left = self.mergeTrees(root1.left,root2.left)
            newNode.val = root1.val + root2.val
            newNode.right = self.mergeTrees(root1.right,root2.right)
        elif root1 == None:
            newNode.left = self.mergeTrees(root1,root2.left)
            newNode.val = root2.val
            newNode.right = self.mergeTrees(root1,root2.right)
        else:
            newNode.left = self.mergeTrees(root1.left,root2)
            newNode.val = root1.val
            newNode.right = self.mergeTrees(root1.right,root2)

        return newNode
