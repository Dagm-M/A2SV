# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)

        def dfs(node):
            
            if node.left:
                adj[node.val].append(node.left.val)
                dfs(node.left)
                adj[node.left.val].append(node.val)

            if node.right:
                adj[node.val].append(node.right.val)
                dfs(node.right)
                adj[node.right.val].append(node.val)

        dfs(root)
        
        q = deque()
        seen = set()
        q.append([target.val,0])
        ans = set()

        while q:
            val,length = q.popleft()
            seen.add(val)
            # print(q,val)

            for ad in adj[val]:
                if ad not in seen and length < k:
                    q.append([ad,length+1])
                elif length == k:
                    ans.add(val)
                seen.add(val)
                # print(q)


        return list(ans)