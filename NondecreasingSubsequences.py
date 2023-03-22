class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()


        def subsequences(curr,arr):
            if curr >= len(nums):
                return

            for i in range(curr,len(nums)):
                if len(arr) == 0 or arr[-1] <= nums[i]:
                    arr.append(nums[i])
                    if len(arr) > 1:
                        ans.add(tuple(arr))
                    subsequences(i+1,arr)
                    arr.pop()

        subsequences(0,[])

        return list(ans)
