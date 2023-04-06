class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for b in board:
            count = Counter(b)
            for key,val in count.items():
                if val > 1 and key != ".":
                    return False
        
        
        for i in range(len(board)):
            count = defaultdict(int)
            for j in range(len(board)):
                count[board[j][i]] += 1
                if count[board[j][i]] > 1 and board[j][i] != ".":
                    return False

        for i in range(3,10,3):
            for j in range(3,10,3):
                count = defaultdict(int)
                for x in range(i-3,i):
                    for y in range(j-3,j):
                        count[board[x][y]] += 1
                        if count[board[x][y]] > 1 and board[x][y] != ".":
                            return False

        return True
