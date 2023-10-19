class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = defaultdict(bool)
        half = sum(nums) 
        if half % 2 != 0:
            return False
        half = half // 2
        def dp(idx,first):
            if idx >= len(nums):
                if first == half:
                    return True
                return False
            if (idx,first) in memo:
                return memo[(idx,first)]
            
            memo[(idx,first)] = dp(idx + 1, first + nums[idx]) or dp(idx + 1, first)

            return memo[(idx,first)]

        return dp(0,0)
