class Solution:
    def countOrders(self, n: int) -> int:
        mod = pow(10, 9) + 7
        ans = 1
        for i in range(n-1):
            num = (n-i) * 2 - 1
            ans *= num * (num + 1) //2
            ans %= mod
            
        return ans
