class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums = list(set(nums))
        nums.sort()
        
        ans = n

        for i, num in enumerate(nums):
            res = num + n - 1
            index = bisect_right(nums,res)

            ans = min(ans, n - (index - i))

        return ans
