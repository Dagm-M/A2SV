class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])

        def get_val(dp, i=0, j=0):
            
            if i == n or j == m:
                return inf
            
            if i == n - 1 and j == m - 1:
                return -dungeon[i][j] + 1 if dungeon[i][j] <= 0 else 1
            
            if dp[i][j] != inf:
                return dp[i][j]
            
            if_we_go_right = get_val(dp, i, j + 1)
            if_we_go_down = get_val(dp, i + 1, j)
            
            min_health_required = min(if_we_go_right, if_we_go_down) - dungeon[i][j]
            
            dp[i][j] = 1 if min_health_required <= 0 else min_health_required
            return dp[i][j]
        
        dp = [[inf] * m for _ in range(n)]
        
        return get_val(dp)
