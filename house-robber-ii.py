class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)

        def houseRob(curr, first):
            if curr >= len(nums):
                return 0

            if curr == len(nums) - 1:
                if first:
                    return 0
                else:
                    return nums[curr]

            if (curr,first) not in memo:
                if curr == 0:
                    temp = houseRob(curr + 2, True) + nums[curr]  
                else:
                    temp = houseRob(curr + 2, first) + nums[curr]

                temp2 = houseRob(curr + 1, first)

                memo[(curr,first)] = max(temp, temp2)

            return memo[(curr, first)]

        
        return houseRob(0, False)