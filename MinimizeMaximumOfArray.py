class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        sum = 0
        res = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            res = max(res, (sum + i) // (i + 1))
        
        
        return res
