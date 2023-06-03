class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        def targetSum(curr,curr_sum):
            if curr >= len(nums):
                if curr_sum == target:
                    return 1
                return 0

            if (curr,curr_sum) not in memo:
                memo[(curr,curr_sum)] = targetSum(curr+1, curr_sum + nums[curr]) + targetSum(curr+1, curr_sum - nums[curr])
            
            return memo[(curr, curr_sum)]

        return targetSum(0, 0)