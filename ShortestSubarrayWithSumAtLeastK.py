class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        minSize = inf
        increasing = deque()
        sum = [0] * (len(nums) + 1)

        for i in range(1 ,len(nums) + 1):
            sum[i] = nums[i - 1] + sum[i-1]


        for right in range(len(sum)):
            
            while len(increasing) > 0 and sum[right] <= sum[increasing[-1]]:
                increasing.pop()

            while len(increasing) > 0 and sum[right] - sum[increasing[0]] >= k:
                minSize = min(minSize, right - increasing[0])
                increasing.popleft()

            increasing.append(right)
            
        if minSize == inf:
            return -1
        
        return minSize
