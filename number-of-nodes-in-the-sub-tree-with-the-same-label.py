class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        ans = [0] * n 
        adj = defaultdict(list)
        seen = defaultdict(int)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        

        def dfs(curr,parent):
            prev = seen[labels[curr]]
            
            for i in adj[curr]:
                if i != parent:
                    dfs(i,curr)

            seen[labels[curr]] += 1
            ans[curr] = seen[labels[curr]] - prev


        dfs(0,-inf)

        return ans