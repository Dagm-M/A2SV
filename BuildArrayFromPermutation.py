class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        permutation = []

        for num in nums:
            permutation.append(nums[num])

        return permutation
