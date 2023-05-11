class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []

        for num in nums:

            while heap and heap[0][0] + 1 < num:
                val = heappop(heap)
                if val[1] < 3:
                    return False

            if not heap or heap[0][0] == num:
                heappush(heap, [num,1]) 

            else:
                val = heappop(heap)
                val[0] += 1
                val[1] += 1
                heappush(heap, val)

        while heap:
            val = heappop(heap)
            if val[1] < 3:
                return False

        return True