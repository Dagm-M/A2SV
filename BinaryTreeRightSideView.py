# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levelNum = defaultdict(list)
        ans = []

        def level(root,l):
            if not root:
                return
           
            levelNum[l].append(root.val)
           
            level(root.left,l+1)
            level(root.right,l+1)
           
            return

        level(root,0)
        for value in levelNum.values():
            ans.append(value[-1])

        return ans
