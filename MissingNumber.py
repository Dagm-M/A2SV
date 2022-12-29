class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # """
        # A solution first by calculating the total sum first
        # """

        # size = len(nums)
        # totalSum = size * (size + 1) / 2
        # sum = 0

        # for num in nums:
        #     sum += num
        
        # return int(totalSum - sum)

        # """
        # A solution with sorting
        # """

        # nums.sort()
        # for i,num in enumerate(nums):
        #     if num != i:
        #         return i
        
        # return len(nums)

        # """
        # A solution with hashmap
        # """

        allNums = []
        
        for i in range(len(nums) + 1):
            allNums.append(i)

        return (set(allNums) - set(nums)).pop()

