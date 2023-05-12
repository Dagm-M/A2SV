class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        q = deque()
        outdegree = defaultdict(list)
        ans = []

        for i,g in enumerate(graph):
            if not g:
                q.append(i)
            for a in g:
                outdegree[a].append(i)
            

        

        while q:
            val = q.popleft()
            ans.append(val)

            for par in outdegree[val]:
                if graph[par]:
                    graph[par].pop()
                if not graph[par]:
                    q.append(par)

        ans.sort()

        return ans