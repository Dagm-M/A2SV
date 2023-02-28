class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        left[0] = nums[0]
        right = [1] * n
        right[n-1] = nums[n-1]
        multiple = [0] * n

        for i in range(1,n):
            left[i] = left[i-1] * nums[i]

        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i]

        multiple[0] = right[1]
        multiple[n-1] = left[n-2]

        for i in range(1,n-1):
            multiple[i] = left[i-1] * right[i+1]

        return multiple
