class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]

        row = self.getRow(rowIndex-1)
        newRow = [1]

        for i in range(1,len(row)):
            newRow.append(row[i] + row[i-1])

        newRow.append(1)

        return newRow
