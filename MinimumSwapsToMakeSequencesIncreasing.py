class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i,w):
            if i >= len(nums1):
                return 0
            if (i,w) in memo:
                return memo[(i,w)]

            res2 = inf
            res = inf
            if i == 0 or (nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]):
   
                res2 = dp(i+1, False)
  
                nums1[i], nums2[i] = nums2[i], nums1[i]
                if i == 0 or nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                    res = dp(i+1, True) + 1
                nums1[i], nums2[i] = nums2[i], nums1[i]
    

            else:
                nums1[i], nums2[i] = nums2[i], nums1[i]
                if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                    res = dp(i+1, True) + 1
                else:
                    return inf
                nums1[i], nums2[i] = nums2[i], nums1[i]
            
            memo[(i,w)] = min(res, res2)

            return memo[(i,w)]

        return  dp(0,False)
