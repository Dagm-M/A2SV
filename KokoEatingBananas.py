class Solution:
    def calculate(self, piles, val):
        total = 0
        for pile in piles:
            total += ceil(pile/val)
        return total
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        ans = piles[-1]
        n = h//len(piles)
        left  = 1
        right = ceil(piles[-1]/n)
        # right = piles[-1]
        
        while left <= right:
            mid = left + (right - left)//2
            time = self.calculate(piles,mid)
            # print(mid,time)

            if time == h:
                while self.calculate(piles,mid) == h:
                    mid -= 1
                return mid + 1
            elif time > h:
                left = mid + 1
            else:
                right = mid - 1
            
            if time <= h and abs(self.calculate(piles,ans) - h) > abs(time - h):
                ans = mid

        return ans
