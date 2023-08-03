class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 1: 
            return 0

        buy = [-10 ** 9] * n
        sell = [0] * n

        for i in range(n):
            sell[i] = max(sell[i - 1], prices[i] + buy[i - 1])
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])

        return sell[-1]
