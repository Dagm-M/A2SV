# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        frequent = defaultdict(int)
        
        def inOrder(root,maximum):
            if not root:
                return maximum

            frequent[root.val] += 1
            maximum = max(maximum, frequent[root.val])

            maximum = max(maximum,inOrder(root.left,maximum))
            maximum = max(maximum,inOrder(root.right,maximum))
            
            return maximum

        maximum = inOrder(root,0)
        ans = []
        for key,val in frequent.items():
            if val == maximum:
                ans.append(key)

        return ans
