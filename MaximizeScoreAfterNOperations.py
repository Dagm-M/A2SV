class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def fn(nums,k):
            if not nums:
                return 0

            ans=0
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    rest=nums[:i]+nums[i+1:j]+nums[j+1:]
                    ans=max(ans,k*gcd(nums[i],nums[j])+fn(tuple(rest),k+1))

            return ans

        return fn(tuple(nums),1)            
