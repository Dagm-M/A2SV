class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        distance = []

        for index in range(len(points)):
            if points[index][0] == x or points[index][1] == y:
                distance.append([abs(x - points[index][0]) + abs(y - points[index][1]), index])
            
        if len(distance) == 0:
            return -1

        distance.sort()

        return distance[0][1]
