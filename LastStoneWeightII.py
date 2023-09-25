class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        memo = defaultdict(int)

        def dp(curr, total):
            if curr >= n:
                return abs(total)

            if (curr,total) not in memo:
                memo[(curr,total)] = min(dp(curr+1, total - stones[curr]), dp(curr +1, total + stones[curr]))

            return memo[(curr,total)]
        
        return dp(0,0)
