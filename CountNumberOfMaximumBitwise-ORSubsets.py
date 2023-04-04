class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subsets = []
        maxNum= 0
        for num in nums:
            maxNum |= num


        def backtrack(arr,index):
 
            if index >= len(nums):
                return

            for i in range(index,len(nums)):
                arr.append(nums[i])
                subsets.append(arr.copy())
                backtrack(arr, i+1)
                arr.pop()


        backtrack([],0)
        total = 0
        for subset in subsets:
            curr = 0
            for i in range(len(subset)):
                curr |= subset[i]
            if curr == maxNum:
                total += 1
        return total
