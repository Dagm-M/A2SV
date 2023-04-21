class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        adj = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        seen = set()

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X" 
            return board           

        def isBound(row,col):
            return (0<=row<len(board)) and (0<=col<len(board[0]))

        def dfs(row,col):

            count = 0
            seen.add((row,col))

            for adjacent in adj:
                new_row = row + adjacent[0]
                new_col = col + adjacent[1]

                if isBound(new_row,new_col) and board[new_row][new_col] == "M":
                    count += 1

            if count == 0:
                for adjacent in adj:
                    new_row = row + adjacent[0]
                    new_col = col + adjacent[1]

                    if isBound(new_row,new_col) and board[new_row][new_col] == "E" and (new_row,new_col) not in seen:
                        dfs(new_row,new_col)

            if count != 0:
                board[row][col] = str(count)
            else:
                board[row][col] = "B"

        dfs(click[0],click[1])

        return board