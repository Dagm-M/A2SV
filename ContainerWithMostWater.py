class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        maxWater = 0

        while left < right:
            con = min(height[left],height[right])
            maxWater = max(maxWater, con * (right - left))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxWater
