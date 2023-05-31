class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        path_val = defaultdict(int)
        path_val[m-1,n-1] = 1
        

        def isBound(row, col):
            return (0 <= row < m) and (0 <= col < n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if isBound(i-1,j):
                    path_val[(i-1,j)] += path_val[(i,j)]
                
                if isBound(i, j-1):
                    path_val[(i, j-1)] += path_val[(i,j)]

        return path_val[(0,0)]