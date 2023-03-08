class Solution:
    def validate(self,nums,threshold,divide):
        sum = 0
        for num in nums:
            sum += ceil(num/divide)
            if sum > threshold:
                return False
        return True

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left = 1
        right = max(nums)

        while left <= right:
            mid = left + (right - left)//2

            if self.validate(nums,threshold,mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
        
        
