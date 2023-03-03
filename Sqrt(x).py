class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x//2
        temp = 0

        if x == 1:
            return 1

        while left <= right:
            mid = left + (right-left)//2
            square = mid*mid

            if square == x:
                return mid
            if square > x:
                right = mid-1
            else:
                left = mid + 1
        
        return right
