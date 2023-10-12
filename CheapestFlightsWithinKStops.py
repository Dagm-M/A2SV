class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, c in flights:
            graph[s].append([d,c])

        ans = inf
        visited = defaultdict(int)
        priority_queue = [(0, src, -1)]
        while priority_queue:
            current_distance, current_node, step = heapq.heappop(priority_queue)
            if step > k:
                continue
            if current_node == dst:
                if step <= k:
                    ans = min(ans, current_distance)
            if current_node in visited:
                if visited[current_node] < step:
                    continue
            visited[current_node] = step

            for neighbor, weight in graph[current_node]:
                heapq.heappush(priority_queue, (current_distance + weight, neighbor, step  + 1))

        return -1 if ans == inf else ans
