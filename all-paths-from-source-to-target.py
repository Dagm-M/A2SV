class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def dfs(adj,arr):
            arr.append(adj)
            if adj == len(graph)-1:
                ans.append(arr.copy())
                return
            
            for i in graph[adj]:
                dfs(i,arr)
                arr.pop()

        dfs(0,[])

        return ans