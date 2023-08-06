class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        Mask = (1<<n) - 1
        ans = []
        cur = []

        def permutations(mask, cur):
            if mask == Mask:
                ans.append(cur[:]) 
                return
            for i in range(n):
                if mask & (1<<i) == 0:
                    cur.append(nums[i])
                    permutations(mask | (1<<i), cur[:]) 
                    cur.pop()

        
        permutations(0, cur)
        return ans
