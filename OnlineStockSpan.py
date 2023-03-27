class StockSpanner:

    dec = []
    def __init__(self):
        self.dec = []

    def next(self, price: int) -> int:
        ans = 1

        while len(self.dec) and self.dec[-1][0] <= price:
            ans += self.dec[-1][1]
            self.dec.pop()
        
        self.dec.append([price,ans])
        
        
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
