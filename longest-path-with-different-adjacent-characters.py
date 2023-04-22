class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        seen = set()
        adj = defaultdict(list)
        longest = 1

        for i in range(1,len(parent)):
            adj[parent[i]].append(i)

        def dfs(index):
            nonlocal longest
            seen.add(index)
            if len(adj[index]) == 0:
                return [s[index],1]

            count = [0,0]
            for i in adj[index]:
                if i not in seen:
                    res = dfs(i)
                    if res[0] != s[index]:
                        count.append(res[1])
            
            count.sort()
            longest = max(longest, count[-1] + count[-2] + 1)

            return [s[index],count[-1]+1]

        dfs(0)

        return longest