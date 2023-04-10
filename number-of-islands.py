class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        seen = set()
        count = 0

        def isBound(row,col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        def dfs(row,col):
            seen.add((row,col))
            for dir in direction:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if isBound(new_row, new_col):
                    if (new_row, new_col) not in seen and grid[new_row][new_col] == "1":
                        dfs(new_row, new_col)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in seen and grid[i][j] == "1":
                    count += 1
                    dfs(i,j)

        return count