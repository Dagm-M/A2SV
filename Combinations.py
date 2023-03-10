class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        #[1,2,3,4]
        def find(nums,k,n,curr):
            if len(nums) == k:
                ans.append(nums.copy())
                return

            for i in range(curr,n+1):
                nums.append(i)
                find(nums,k,n,i+1)
                nums.pop()

        find([],k,n,1)

        return ans
