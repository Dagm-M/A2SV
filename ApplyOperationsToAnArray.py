class Solution:
    def moveZeroes(self, nums: List[int]):
        write = 0
        read = 0

        while read < len(nums):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
            
                write =  write + 1
            
            read = read + 1

            
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums) -1):
            if nums[index] == nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0

        self.moveZeroes(nums)
        

        return nums
