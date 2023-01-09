class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        size = len(nums)
        numDict = {}

        for index,num in enumerate(nums):
            numDict[num] = index

        for num,value in operations:
            if num in numDict:
                nums[numDict[num]] = value
                numDict[value] = numDict[num]

        return nums       
