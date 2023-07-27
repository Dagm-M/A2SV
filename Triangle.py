class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        temp = triangle[-1].copy()

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                temp[j] = triangle[i][j] + min(temp[j], temp[j+1])
                
        return temp[0]
