class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = []

        for x in range(1, query_row + 2):
            dp.append([0] * x)

        dp[0][0] = poured
        
        for i in range(query_row):
            for j in range(len(dp[i])):
                temp = (dp[i][j] - 1) / 2.0
                if temp>0:
                    dp[i+1][j] += temp
                    dp[i+1][j+1] += temp

        if dp[query_row][query_glass] < 1:
            return dp[query_row][query_glass]
        else:
            return 1
