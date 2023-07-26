class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ans = []
        indegree = [0] * n
        parent_child = defaultdict(set)

        for i in range(n):
            ans.append(set())

        for a, b in edges:
            ans[b].add(a)
            parent_child[a].add(b)
            indegree[b] += 1

        dq = deque()

        for i, inde in enumerate(indegree):
            if inde == 0:
                dq.append(i)

        while dq:
            temp = dq.popleft()

            for b in parent_child[temp]:
                ans[b].update(ans[temp])
                indegree[b] -= 1
                if indegree[b] == 0:
                    dq.append(b)

        temp2 = []

        for a in ans:
            temp2.append(sorted(a))

        return temp2
