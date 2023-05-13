class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        total = 0

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])


        def dfs(node,length,parent):
            nonlocal total
            nodebefore = 0
            if hasApple[node]:
                total += length
                length = 0

            for ad in adj[node]:
                if ad != parent:
                    nodebefore += dfs(ad, length + 1, node)
                    if nodebefore or hasApple[ad]:
                        length = 0
            
            if hasApple[node]:
                nodebefore += 1
            return nodebefore


        dfs(0,0,None)

        return total * 2