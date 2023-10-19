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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = self.inOrder(root)

        return arr[k-1]
