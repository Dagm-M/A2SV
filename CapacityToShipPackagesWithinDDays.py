class Solution:
    def possible(self,weights,days,mid):
        total = 0
        day = 0
        for weight in weights:
            if total + weight <= mid:
                total += weight
            else:
                total = 0
                total += weight
                day += 1
            
        if total > 0:
            day += 1

        return day <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = 1

        while left <= right:
            mid = left + (right - left)//2

            if self.possible(weights,days,mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
        
