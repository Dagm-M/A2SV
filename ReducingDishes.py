class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        dp = [[-1] * 501 for i in range(501)]

        def solve(tk, idx):
            if idx == len(satisfaction):
                return 0
            temp = dp[tk][idx]

            if temp != -1:
                return temp
                
            temp = max(solve(tk, idx + 1), tk * satisfaction[idx] + solve(tk + 1, idx + 1))
            dp[tk][idx] = temp
            return temp
        

        
        return solve(1,0)
