class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            while (i+1) != nums[i] and nums[i] != nums[nums[i] -1]:
                temp = nums[i]
                nums[i],nums[temp-1] = nums[temp-1],temp
        
        for i in range(len(nums)):
            if (i+1) != nums[i]:
                ans = [nums[i], i+1]

        return ans
