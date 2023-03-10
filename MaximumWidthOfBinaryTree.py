# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelNum = defaultdict(list)
        maximum = 0

        def level(root,l,pos):
            if not root:
                return
           
            levelNum[l].append(pos)
           
            level(root.left,l+1,(2*pos)+1)
            level(root.right,l+1,(2*pos)+2)
           
            return

        level(root,0,0)
        for value in levelNum.values():
            maximum = max(value[-1] - value[0] + 1,maximum)

        return maximum
