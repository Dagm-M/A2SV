class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp =defaultdict(int)

        def sol(targ):
            if targ == 0:
                return 1
            elif targ < 0:
                return 0
            elif targ in dp:
                return dp[targ]

            ans = 0

            for i in range(len(nums)):
                ans += sol(targ - nums[i])

            dp[targ] = ans

            return dp[targ]

        return sol(target)
