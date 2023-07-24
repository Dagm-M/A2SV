class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        ans = 1

        for i in arr:
            if i - difference in dp:
                dp[i] = dp[i - difference] + 1
                ans = max(ans, dp[i])
            else:
                dp[i] = 1

        return ans
