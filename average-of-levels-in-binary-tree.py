# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append([root,0])
        levels = defaultdict(list)
        ans = []

        while queue:

            node,level = queue.popleft()
            temp = levels[level]
            if len(temp):
                temp[0] += node.val
                temp[1] += 1
                levels[level] = temp
            else:
                levels[level] = [node.val,1]

            if node.left:
                queue.append((node.left,level+1))
            
            if node.right:
                queue.append((node.right,level+1))

        for val in levels.values():
            ans.append(val[0] / val[1])

        return ans