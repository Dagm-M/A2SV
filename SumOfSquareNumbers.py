class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))

        while left <= right:
            if pow(left,2) + pow(right,2) < c:
                left += 1
            elif pow(left,2) + pow(right,2) > c:
                right -= 1
            else:
                return True

        return False

        
        
