class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        maxCoins = 0

        for index in range(1,len(piles) - len(piles)//3,2):
            maxCoins += piles[index]

        return maxCoins
