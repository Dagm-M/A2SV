class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        for index in range(n):
            num = nums[index]
            result = 0
            while num != 0:
                remn = num % 10
                num = num//10
                result *= 10
                result += remn
            nums.append(result)

        nums = set(nums)

        return len(nums)
