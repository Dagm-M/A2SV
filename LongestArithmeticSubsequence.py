class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        
        for i in range(len(nums)):
            for j in range(0, i):
                if dp[(j, nums[i] - nums[j])]:
                    dp[(i, nums[i] - nums[j])] = dp[(j, nums[i] - nums[j])] + 1
                else:
                    dp[(i, nums[i] - nums[j])] = 2
        
        return max(dp.values())
