class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = defaultdict(int)
        n = len(nums1)
        m = len(nums2)
        def dp(i, j):
            if i >= n or j >= m:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]
            
            if nums1[i] == nums2[j]:
                memo[(i,j)] = dp(i+1, j+1) + 1
            else:
                memo[(i,j)] = max(dp(i, j+1), dp(i+1, j))

            return memo[(i,j)]

        return dp(0,0)
