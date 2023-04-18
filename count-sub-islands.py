class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        seen = set()
        curr_seen = set()
        count = 0

        def isBound(row,col):
            return (0 <= row < len(grid2)) and (0 <= col < len(grid2[0]))

        def dfs(row,col):

            seen.add((row,col))
            curr_seen.add((row,col))
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if isBound(new_row,new_col)  and grid2[new_row][new_col] == 1 and (new_row,new_col) not in curr_seen:
                    if grid1[new_row][new_col] == 1 and (new_row,new_col) not in seen:
                        if not dfs(new_row,new_col):
                            return False
                    else:
                        return False

            return True


        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i,j) not in seen and grid2[i][j] == 1 and grid1[i][j] == 1:
                    temp = dfs(i,j)
                    if temp:
                        count += 1
                    curr_seen.clear()

        return count