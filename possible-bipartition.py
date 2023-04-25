class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        seen = defaultdict(int)
        adj = defaultdict(list)
        ans = True

        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        def dfs(curr,prevGroup):

            seen[curr] = 1 - prevGroup

            for i in adj[curr]:
                if i not in seen:
                    res = dfs(i,seen[curr])
                    if not res:
                        return False
                elif seen[i] == seen[curr]:  
                    return False

            return True

        for ad in adj.keys():
            if ad not in seen:
                ans = ans and dfs(ad, 1)

            if not ans:
                break

        return ans