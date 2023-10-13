class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        seen = set()
        ans = 0

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            nonlocal ans

            total = 0
            seen.add(node)
            for nxt in graph[node]:
                if nxt not in seen:
                    total += dfs(nxt)
            
            if (values[node] + total) % k == 0:
                ans += 1
                return 0
            else:
                return values[node] + total

        dfs(0)
        return ans
