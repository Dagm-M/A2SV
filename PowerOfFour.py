class Solution:
    def isPowerOfFour(self, n: int, k = 1) -> bool:

        if k == n:
            return True
        
        if k > n:
            return False

        return self.isPowerOfFour(n,k*4)
