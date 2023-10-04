class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, w in times:
            graph[s-1].append([d-1,w])

        distances = [inf for i in range(n)]
        distances[k-1] = 0
        visited = set() 
        priority_queue = [(0, k-1)]
        while priority_queue:
            current_distance, current_node = heappop(priority_queue)
            if current_node in visited:
                continue
            visited.add(current_node)
            
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(priority_queue, (distance, neighbor))

        temp = max(distances) 
        if temp != inf:
            return temp
        return -1
