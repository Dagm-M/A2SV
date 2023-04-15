class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        max_area = 0
        count = 0
        seen = set()

        def isBound(row,col):
            return (0<=row<len(grid)) and (0<=col<len(grid[0]))

        def dfs(row,col):
            nonlocal count
            count += 1
            seen.add((row,col))

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if isBound(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row,new_col) not in seen:
                    dfs(new_row,new_col)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = 0
                if grid[i][j] == 1 and (i,j) not in seen:
                    dfs(i,j)
                    max_area = max(max_area,count)


        return max_area