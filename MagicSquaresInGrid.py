class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        counter = 0

        if n < 3 or m < 3:
            return 0
        
        for i in range(3,n+1):
            for j in range(3,m+1):
                same = grid[i-3][j-3] + grid[i-2][j-2] + grid[i-1][j-1]
                didBreak = False
                count = defaultdict(int)
                for x in range(i-3,i):
                    total = 0
                    for y in range(j-3,j):
                        total += grid[x][y]
                        count[grid[x][y]] += 1

                        if (count[grid[x][y]] > 1) or (grid[x][y] > 9) or (grid[x][y] < 1):
                            didBreak = True
                            break
                    if (total != same):
                        didBreak = True
                        break

                if not didBreak:
                    for x in range(j-3,j):
                        total = 0
                        for y in range(i-3,i):
                            total += grid[y][x]
                        if total != same:
                            didBreak = True
                            break

                if grid[i-3][j-1] + grid[i-2][j-2] + grid[i-1][j-3] != same:
                    didBreak = True
                    
                if not didBreak:
                    counter += 1

        return counter
