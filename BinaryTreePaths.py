# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        arr = []

        def find(root,path):
            if not root.left and not root.right:
                path.append(str(root.val))
                arr.append("".join(path))
                return 

            path.append(str(root.val))
            path.append("->")
            if root.left:
                find(root.left,path.copy())
            if root.right:
                find(root.right,path.copy())

        find(root,[])

        return arr
