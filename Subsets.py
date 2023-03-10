class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = [[]]

        def subset(arr,curr):
            if curr >= len(nums):
                return

            for i in range(curr,len(nums)):
                arr.append(nums[i])
                sub.append(arr.copy())
                subset(arr,i+1)
                arr.pop()
        
        subset([],0)

        return sub
