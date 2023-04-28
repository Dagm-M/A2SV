class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        count = inf
        directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        q = deque()
        if grid[0][0] == 0:
            q.append([(0,0),1])
        seen = set()
        n = len(grid)

        def isBound(row,col):
            return (0 <= row < n) and (0 <= col < n)

        while q:
            val,parent = q.popleft()
            seen.add(val)
            if val == (n-1, n-1):
                count = min(count, parent)
                return count

            for direction in directions:
                new_row = val[0] + direction[0]
                new_col = val[1] + direction[1]

                if isBound(new_row, new_col) and (new_row,new_col) not in seen and grid[new_row][new_col] == 0:
                    seen.add((new_row,new_col))
                    q.append([(new_row,new_col),parent+1])

        
        return -1