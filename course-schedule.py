class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ans = 0

        adj = defaultdict(list)
        color = defaultdict(int)

        for courses in prerequisites:
            adj[courses[1]].append(courses[0])
            color[courses[1]] = 0
            color[courses[0]] = 0


        def dfs(node):
            nonlocal ans
            color[node] += 1

            for ad in adj[node]:
                if color[ad] == 0:
                    dfs(ad)
                elif color[ad] == 1:
                    return

            color[node] += 1
            ans += 1
                
        for i in range(numCourses):
            if color[i] == 0:
                dfs(i)

        if ans == numCourses:
            return True

        return False