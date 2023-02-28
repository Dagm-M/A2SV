class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sum = 0
        count = 0
        seen = defaultdict(int)

        for num in nums:
            sum += num
            
            if sum-k in seen:
                count += seen[sum-k]

            seen[sum] += 1

            if sum == k:
                count += 1
        
        return count
