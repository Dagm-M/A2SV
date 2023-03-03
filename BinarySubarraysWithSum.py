class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        sub = 0

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        for num in nums:
            if (num - goal) in seen:
                sub += seen[num-goal]
            
            if num - goal == 0:
                sub += 1
            
            seen[num] += 1

        return sub
