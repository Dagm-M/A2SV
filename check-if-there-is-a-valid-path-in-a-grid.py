class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        seen = set()


        q = deque()
        q.append([0,0])

        def isBound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        def isCompatable(direction, a, b):
            if direction == [0,1]: #right 
                if a == 1 and b in {1,3,5}:
                    return True
                elif a == 4 and b in {1,5,3}:
                    return True
                elif a == 6 and b in {1,3,5}:
                    return True
            if direction == [0,-1]: #left
                if a == 1 and b in {1,4,6}:
                    return True
                if a == 3 and b in {1,4,6}:
                    return True
                if a == 5 and b in {1,4,6}:
                    return True
            if direction == [1,0]: #Down:
                if a == 2 and b in {2,5,6}:
                    return True
                if a == 3 and b in {2, 5,6}:
                    return True
                if a == 4 and b in {2, 5, 6}:
                    return True
            if direction == [-1,0]: #up:
                if a == 2 and b in {2,3,4}:
                    return True
                if a == 5 and b in {2,3,4}:
                    return True
                if a == 6 and b in {2,3,4}:
                    return True

        while q:
            row,col = q.popleft()
            seen.add((row,col))
            if [row, col] == [len(grid)-1 , len(grid[0])-1]:
                    return True

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if isBound(new_row, new_col) and (new_row, new_col) not in seen and isCompatable(direction, grid[row][col], grid[new_row][new_col]):
                    if [new_row,new_col] == [len(grid)-1 , len(grid[0])-1]:
                        return True
                    q.append([new_row,new_col])
                    seen.add((new_row,new_col))

        return False