class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        bricks_used = []
        
        for i in range(1,len(heights)):
            diff = heights[i] - heights[i-1]
            if  diff > 0:
                if bricks - diff >= 0:
                    bricks -= diff
                    heappush(bricks_used,-diff)
                else:
                    if ladders == 0:
                        return i - 1
                    if len(bricks_used) and -bricks_used[0] >= diff:
                        bricks += -heappop(bricks_used)
                        bricks -= diff
                        heappush(bricks_used, -diff)
                    ladders -= 1

        return len(heights) - 1