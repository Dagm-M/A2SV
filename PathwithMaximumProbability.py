class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        seen = set()
        for i,(a,b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        heap = [(0,start_node)]

        while len(heap) != 0:
            probability, node = heappop(heap)

            if node == end_node:
                return 1 - probability
            
            if node in seen:
                continue
            seen.add(node)

            for nxt_node, prob in graph[node]:
                nxt_prob = 1 - ((1 - probability) * prob)
                heappush(heap, (nxt_prob, nxt_node))
        
        return 0
