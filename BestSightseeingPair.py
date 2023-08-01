class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        sum = values[0]
        for i in range(1, len(values)):
            ans = max(ans , sum + values[i] - i)
            sum = max(sum, values[i] + i)

        return ans
