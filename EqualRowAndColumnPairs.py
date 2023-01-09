class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        colTable = []
        counter = 0

        for index in range(len(grid[0])):
            temp = []
            for row in grid:
                temp.append(row[index])

            colTable.append(tuple(temp))

        colTable = Counter(colTable)
        
        for row in grid:
            row = tuple(row)
            if row in colTable:
                counter += colTable[row]

        return counter
