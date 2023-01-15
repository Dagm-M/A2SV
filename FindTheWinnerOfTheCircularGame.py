class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = []

        for num in range(1, n + 1):
            nums.append(num)

        start = 0
        while(len(nums) > 1):
            l = len(nums)
            nums.remove(nums[(start+k-1)%len(nums)])
            start = (start+k-1)%l
        return nums[0]
