class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left = 0
        sum = 0
        maximum = -inf
        

        for right in range(len(nums)):

            sum += nums[right]

            if right - left + 1 == k:
                avg = sum/k
                maximum= max(maximum,avg)
                sum -= nums[left]
                left += 1

        return maximum


