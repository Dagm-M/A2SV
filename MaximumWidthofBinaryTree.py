# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append([root, 0, 0])
        difference = defaultdict(list)
        ans = 0


        while queue:
            node, level, pos = queue.popleft()

            if node.left:
                queue.append([node.left, level + 1, 2 * pos + 1])


            if node.right:
                queue.append([node.right, level + 1, 2 * pos + 2])

            
            if len(difference[level]) > 1:
                difference[level].pop()
            difference[level].append(pos)


        for diff in difference.values():
            ans = max(ans, diff[-1] - (diff[0] - 1))

        return ans  
