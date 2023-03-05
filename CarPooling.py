class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        position = [0] * 1001

        for trip in trips:
            position[trip[1]] += trip[0]
            position[trip[2]] -= trip[0]

        if position[0] > capacity:
            return False

        for i in range(1,len(position)):
            position[i] += position[i-1]

            if position[i] > capacity:
                return False

        return True
