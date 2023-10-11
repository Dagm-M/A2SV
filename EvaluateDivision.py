class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(int)
        s = set()
        ans = []

        for i,(a,b) in enumerate(equations):
            graph[(a,b)] = values[i]
            graph[(b,a)] = 1 / values[i]
            graph[(a,a)] = 1.0
            graph[(b,b)] = 1.0
            s.add(a)
            s.add(b)

        n = len(s)

        for k in s:
            for i in s:
                for j in s:
                    if (i,j) not in graph:
                        graph[(i,j)] = inf
                    if (i,k) not in graph:
                        graph[(i,k)] = inf
                    if (k,j) not in graph:
                        graph[(k,j)] = inf
                    
                    graph[(i,j)] = min(graph[(i,j)], graph[(i,k)] * graph[(k,j)]) 

        
        for a,b in queries:
            if (a,b) in graph:
                if graph[(a,b)] == inf:
                    ans.append(-1.0)
                else:
                    ans.append(graph[(a,b)])
            else:
                ans.append(-1.0)

        return ans
