class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 0

        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        if x == 1:
            return 1

        ans = x * x
        if n % 2 == 0:
            return self.myPow(ans,n/2)
        else:
            if n > 0:
                return self.myPow(ans,n//2) * x
            else:
                return self.myPow(ans,ceil(n/2)) * 1/x
