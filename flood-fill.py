class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        start = image[sr][sc]

        def isBound(row,col):
            return (0 <= row < len(image)) and (0 <= col < len(image[0]))
        
        def dfs(row,col):

            seen.add((row,col))
            if image[row][col] == start:
                image[row][col] = color

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if isBound(new_row,new_col) and image[new_row][new_col] == start and (new_row,new_col) not in seen:
                    dfs(new_row,new_col)

        dfs(sr,sc)

        return image