class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while (i+1) != nums[i]:
                if nums[i] == nums[nums[i] -1]:
                    return nums[i]
                temp = nums[i]
                nums[i],nums[temp-1] = nums[temp-1],temp
