class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ans = []
        seen = set()

        if not nums1 or not nums2:
          return []

        heappush(heap, [nums1[0] + nums2[0], 0, 0])
        seen.add((0,0))
        

        while len(ans) < k and heap:
          val = heappop(heap)
          ans.append([nums1[val[1]], nums2[val[2]]])

          if val[1] + 1 < len(nums1) and (val[1]+1, val[2]) not in seen:
            heappush(heap, [nums1[val[1] + 1] + nums2[val[2]], val[1] + 1, val[2]])
            seen.add((val[1] + 1, val[2]))

          if val[2] + 1 < len(nums2) and (val[1], val[2]+1) not in seen:
            heappush(heap, [nums1[val[1]] + nums2[val[2] + 1], val[1], val[2] + 1])
            seen.add((val[1], val[2] + 1))
        
        return ans
