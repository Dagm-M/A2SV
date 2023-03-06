class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        

        if len(nums) == 0:
            return ans
        
        ans = [bisect_left(nums,target),bisect_right(nums,target) - 1]

        if nums[ans[1]] != target:
            ans = [-1,-1]

        return ans
