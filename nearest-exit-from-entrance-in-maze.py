class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def isBound(row, col):
            return (0 <= row < len(maze)) and (0 <= col < len(maze[0]))

        q = deque()
        q.append([entrance,0])
        seen = set()
        


        while q:
            val,length = q.popleft()

            seen.add((val[0],val[1]))


            for direction in directions:
                new_row = val[0] + direction[0]
                new_col = val[1] + direction[1]

                if isBound(new_row,new_col) and (new_row,new_col) not in seen and maze[new_row][new_col] == ".":
                    if (new_row == len(maze) - 1 or new_col == len(maze[0]) - 1 or new_row == 0 or new_col == 0):
                        return length + 1
                    q.append([[new_row,new_col],length+1])

                seen.add((new_row,new_col))



        return -1