class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        degree = defaultdict(int)
        seen = set()
        ans = []

        for adjacent in adjacentPairs:
            adj[adjacent[0]].append(adjacent[1])
            adj[adjacent[1]].append(adjacent[0])
            degree[adjacent[0]] += 1
            degree[adjacent[1]] += 1

        q = deque()
        for key,item in degree.items():
            if item == 1:
                q.append(key)
                degree[key] -= 1
                break

        while q:
            val = q.popleft()
            ans.append(val)
            seen.add(val)

            for ad in adj[val]:
                if ad not in seen:
                    q.append(ad)
                seen.add(ad)
                
        return ans