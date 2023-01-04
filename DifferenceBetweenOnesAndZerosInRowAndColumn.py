class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowSum = []
        colSum = []
        diff = []


        for row in grid:
            rowSum.append(Counter(row)[1])

        for row in grid:
            for colindex in range(len(row)):
                if len(colSum) == len(row):
                    colSum[colindex] += row[colindex]
                else:
                    colSum.append(row[colindex])
            

        for rowindex in range(len(rowSum)):
            tempRow = []
            for colindex in range(len(colSum)):
                tempRow.append(rowSum[rowindex] + colSum[colindex] - (len(rowSum) - rowSum[rowindex]) - (len(colSum) - colSum[colindex]))
            
            diff.append(tempRow)

        return diff
