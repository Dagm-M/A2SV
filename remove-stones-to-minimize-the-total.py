class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        for i in range(len(piles)):
            piles[i] *= -1

        heapify(piles)

        for i in range(k):
            val = heappop(piles) * -1
            temp = val //2
            val -= temp
            heappush(piles,val * -1)

        return sum(piles) * -1