class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(set)
        max_rank = 0

        for road in roads:
            adj[road[0]].add(road[1])
            adj[road[1]].add(road[0])

        for key, negibors in adj.items():
            rank = len(negibors)

            for k in adj.keys():
                if k == key:
                    continue
                if k in negibors:
                    new_rank = rank + len(adj[k]) - 1
                else:
                    new_rank = rank + len(adj[k])

                max_rank = max(max_rank, new_rank)


        
        return max_rank