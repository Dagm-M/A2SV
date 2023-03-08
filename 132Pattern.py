class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        temp = -inf
        stack = []

        for i in range(len(nums)-1,-1,-1):
            if nums[i] < temp:
                return True

            while len(stack) != 0 and nums[i] > stack[-1]:
                temp = stack[-1]
                stack.pop()

            stack.append(nums[i])

        return False
