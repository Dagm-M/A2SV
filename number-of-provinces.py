class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        adjList = defaultdict(list)

        for i in range(size):
            for j in range(size):
                if isConnected[i][j] == 1 and i != j:
                    adjList[i+1].append(j+1)

        seen = set()
        count =0

        def dfs(negbor):
            seen.add(negbor)
            for i in adjList[negbor]:
                if i not in seen:
                    dfs(i)

        for i in range(1,size+1):
            if i not in seen:
                dfs(i)
                count += 1

        return count