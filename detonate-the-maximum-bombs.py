class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        max_bombs = 0
        seen = set()
        adj = defaultdict(list)

        def distance(x1,y1,x2,y2):
            return pow((pow(x2-x1,2)+pow(y2-y1,2)), 0.5)

        for i,bomb in enumerate(bombs):
            radius = bomb[2]
            for j,bom in enumerate(bombs):
                dis = distance(bomb[0],bomb[1],bom[0],bom[1])
                if dis <= radius:
                    adj[i].append(j)

        def dfs(index):
            nonlocal max_bombs
            seen.add(index)

            for i in adj[index]:
                if i not in seen:
                    dfs(i)

        for i in range(len(bombs)):
            dfs(i)
            max_bombs= max(max_bombs,len(seen))
            seen.clear()

        return max_bombs