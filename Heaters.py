class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = -inf
        heaters.sort()

        for house in houses:
            index = bisect_left(heaters,house)
            if index < len(heaters) and heaters[index] == house:
                radius = max(radius, 0)
            else:
                if index == 0:
                    radius = max(radius, abs(heaters[index] - house))
                elif index == len(heaters):
                    radius = max(radius, abs(heaters[index - 1] - house))
                else:
                    temp = min(abs(heaters[index] - house),abs(heaters[index-1] - house))
                    radius = max(radius, temp)

        return radius
