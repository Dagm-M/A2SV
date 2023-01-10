class Solution:
    def whoWon(self, board) -> list:
        winner = "Z"
        numX = 0
        numO = 0

        #For the horizontal wins
        for tic in board:
            if tic == "XXX":
                winner += "X"
            elif tic == "OOO":
                winner += "O"

        #For the virtical wins
        for num in range(3):
            temp = []
            for tic in board:
                temp.append(tic[num])
                if tic[num] == "X":
                    numX += 1
                if tic[num] == "O":
                    numO += 1

            if temp == ["X","X","X"]:
                winner += "X"
            elif temp == ["O","O","O"]:
                winner += "O"

        if [board[0][0], board[1][1], board[2][2]] == ["X","X","X"]:
            winner += "X"
        elif [board[0][0], board[1][1], board[2][2]] == ["O","O","O"]:
            winner += "O"

        if [board[0][2], board[1][1], board[2][0]] == ["X","X","X"]:
            winner += "X"
        elif [board[0][2], board[1][1], board[2][0]] == ["O","O","O"]:
            winner += "O"

        return [winner,numX, numO]
        
    def validTicTacToe(self, board: List[str]) -> bool:

        result = self.whoWon(board)

        if result[0] == "Z" and (result[1] == result[2] or result[1] == (result[2] + 1)):
            return True
        elif result[0] == "ZX" and (result[1] == (result[2] + 1)):
            return True
        elif result[0] == "ZO" and (result[1] == result[2]):
            return True
        elif result[1] == 5 and result[2] == 4 and result[0] == "ZXX":
            return True
        

        return False
