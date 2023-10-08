class Solution:
    def knightDialer(self, n: int) -> int:
        directions = [[-2,1],[-2,-1],[-1,-2],[-1,2],[1,2],[1,-2],[2,-1],[2,1]]
        grid = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
        mod = pow(10,9) + 7
        
        memo = defaultdict(int)
        isBound = lambda r, c : -1 < r < 4 and -1 < c < 3
        def dp(n, r,c):
            if grid[r][c] == -1:
                return 0
            if n == 1:
                return 1

            if (n, r,c) in memo:
                return memo[(n, r,c)]

            res = 0
            for direction in directions:
                nR = r + direction[0]
                nC = c + direction[1]
                if isBound(nR, nC) and grid[nR][nC] != -1:
                    res += dp(n - 1, nR, nC)
            
            memo[(n, r,c)] = res

            return memo[(n, r,c)]

        ans = 0
        for i in range(4):
            for j in range(3):
                ans += dp(n, i, j)

        return ans % mod
