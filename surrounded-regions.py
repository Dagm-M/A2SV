class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        seen = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def isBound(row,col):
            return (0 <= row < len(board)) and (0 <= col < len(board[0]))

        def dfs(row,col):
            seen.add((row,col))

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if isBound(new_row,new_col) and (new_row,new_col) not in seen and board[new_row][new_col] == "O":
                    dfs(new_row,new_col)

        row_temp = [0,len(board)-1]
        col_temp = [0,len(board[0])-1]

        for i in row_temp:
            for j in range(len(board[0])):
                if (i,j) not in seen and board[i][j] == "O":
                    dfs(i,j)

        for i in range(len(board)):
            for j in col_temp:
                if (i,j) not in seen and board[i][j] == "O":
                    dfs(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in seen and board[i][j] == "O":
                    board[i][j] = "X"