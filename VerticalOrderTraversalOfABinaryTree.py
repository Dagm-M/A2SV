# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelNum = defaultdict(list)
        temp = []

        def level(root,l,y):
            if not root:
                return
           
            levelNum[y].append([l,root.val])
           
            level(root.left,l+1,y-1)
            level(root.right,l+1,y+1)
           
            return

        level(root,0,0)
        for key in levelNum.keys():
            temp.append(key)

        temp.sort()
        temp2 = []

        for val in temp:
            levelNum[val].sort()
            temp3 = []
            for item in levelNum[val]:
                temp3.append(item[1])
            temp2.append(temp3)
        
        return temp2
