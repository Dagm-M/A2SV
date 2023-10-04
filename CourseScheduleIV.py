class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        ans = []
        dist = [[False] * numCourses for _ in range(numCourses)]

        for a, b in prerequisites:
            dist[a][b] = True


        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dist[i][j] = dist[i][j] or (dist[i][k] and dist[k][j])

        for a,b in queries:
            ans.append(dist[a][b])

        return ans
