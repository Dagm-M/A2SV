class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans = [n for n in range(len(quiet))]
        indegree = [0] * len(quiet)
        richer_less = defaultdict(set)

        for a, b in richer:
            if quiet[ans[a]] < quiet[ans[b]]:
                ans[b] = ans[a]
            richer_less[a].add(b)
            indegree[b] += 1

        dq = deque()

        for i, inde in enumerate(indegree):
            if inde == 0:
                dq.append(i)

        while dq:
            temp = dq.popleft()

            for b in richer_less[temp]:
                if quiet[ans[temp]] < quiet[ans[b]]:
                    ans[b] = ans[temp]
                indegree[b] -= 1
                if indegree[b] == 0:
                    dq.append(b)


        return ans
