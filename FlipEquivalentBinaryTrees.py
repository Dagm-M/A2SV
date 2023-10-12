# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        def bfs(node, node2):
            if not node and not node2:
                return True
            if not node and node2 or not node2 and node:
                return False
            queue = deque([node])
            queue2 = deque([node2])

            while queue:
                node = queue.popleft()
                node2 = queue2.popleft()

                if node.val != node2.val:
                    return False

                if (not node.left and node2.left) or (not node2.left and node.left):
                    node2.left, node2.right = node2.right, node2.left
                    if (not node.left and node2.left) or (not node2.left and node.left):
                        return False
                if (not node.right and node2.right) or (not node2.right and node.right):
                    return False

                inLeft = False
                if node.left:
                    if node.left.val != node2.left.val:
                        inLeft = True
                        node2.left, node2.right = node2.right, node2.left
                        if node.left.val != node2.left.val:
                            return False
                        if node.right and node.right.val != node2.right.val:
                            return False

                if node.right:
                    if node.right.val != node2.right.val:
                        if not inLeft:
                            node2.left, node2.right = node2.right, node2.left
                            if node.right.val != node2.right.val:
                                return False
                            if node.left and node.left.val != node2.left.val:
                                return False

                if node.left:
                    queue.append(node.left)
                    queue2.append(node2.left)

                if node.right:
                    queue.append(node.right)
                    queue2.append(node2.right)

            return True
                
        return bfs(root1, root2)
