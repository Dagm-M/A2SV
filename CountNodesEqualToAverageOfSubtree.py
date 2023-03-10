# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def average(root):
            nonlocal count
            if not root.left and not root.right:
                count += 1
                return [root.val,1]


            left, right = 0,0
            L,R = 0,0
            if root.left:
                left,L = average(root.left)

            if root.right:
                right,R = average(root.right)

            sum = left + right + root.val
            nodes = L+R+1
            avg = sum//nodes

            if avg == root.val:
                count += 1

            return [sum,nodes]

        average(root)

        return count
