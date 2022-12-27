class Solution:
    def checkTriangle(self, sideA, sideB, sideC):
        return (sideA + sideB) > sideC and (sideC + sideB) > sideA and (sideA + sideC) > sideB

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for index in range(len(nums) - 3, -1, -1):
            if self.checkTriangle(nums[index], nums[index + 1], nums[index + 2]):
                return nums[index] + nums[index + 1] + nums[index + 2]


        return 0
