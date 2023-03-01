class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort()
        count = 1
        slowestTime = 0

        for i in range(len(cars) - 2, -1, -1):
            next = (target - cars[i + 1][0])/ cars[i + 1][1]
            curr = (target - cars[i][0])/ cars[i][1]

            slowestTime = max(slowestTime, next)

            if slowestTime < curr:
                count += 1

        return count
