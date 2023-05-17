class Solution(object):
    def minimumTime(self, n, edges):
        depend = defaultdict(int)
        adj = defaultdict(list)
        ans = [0] * n
        seen = set()
        time = 1
        parent = defaultdict(set)


        for edge in edges:
            adj[edge[0]].append(edge[1])
            parent[edge[1]].add(edge[0])
            depend[edge[1]] += 1

        q = deque()

        for val in range(n):
            if depend[val] == 0:
                q.append(val)
                ans[val] = time
            parent[val].add(val)
        count = 0

        while q:
            if count == 0:
                time += 1
                count = len(q)
            val = q.popleft()
            count -= 1
            
            
            seen.add(val)
            
            for ad in adj[val]:
                depend[ad] -= 1
                if ad not in seen and depend[ad] < 1:
                    q.append(ad)
                    ans[ad] = time
                    seen.add(ad)
                # print(val,ad)
                # print(parent[val])
                for i in parent[val]:
                    parent[ad].add(i)
                # parent[ad].union(parent[val])
                # print(parent[ad])

        return [ans, parent]
        
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):

        level, parent = self.minimumTime(numCourses, prerequisites)
        ans = []

        for a,b in queries:

            if level[a] < level[b] and a in parent[b]:
                ans.append(True)
            else:
                ans.append(False)


        return ans