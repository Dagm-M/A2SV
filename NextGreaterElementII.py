class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        DecStack = []
        n = len(nums)
        nextGreater = [0] * n

        for i in range((n-1)*2, -1, -1):
            
            while len(DecStack) != 0 and DecStack[-1] <= nums[i % n]:
                DecStack.pop()

            if len(DecStack) == 0:
                nextGreater[i % n] = -1
            else:
                nextGreater[i % n] = DecStack[-1]

            DecStack.append(nums[i % n])

        return nextGreater
