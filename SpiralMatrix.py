class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowSize = len(matrix)
        colSize = len(matrix[0])
        totalSize = rowSize * colSize
        spiral = []
        offset = 0

        # if there is a number in the matrix dont exit
        while totalSize > 0:

            row = offset
            col = offset

            # getting the upper row
            while col < colSize:
                spiral.append(matrix[row][col])
                col += 1
                totalSize -= 1

            if totalSize <= 0:
                break

            row += 1
            col -= 1
            # getting the right colomn
            while row < rowSize:
                spiral.append(matrix[row][col])
                row += 1
                totalSize -= 1

            if totalSize <= 0:
                break

            col -= 1
            row -= 1
            # getting the lower row
            while col >= offset:
                spiral.append(matrix[row][col])
                col -= 1
                totalSize -= 1


            if totalSize <= 0:
                break

            

            row -= 1
            col += 1
            # getting the left colomn
            while row >= (offset + 1):
                spiral.append(matrix[row][col])
                row -= 1
                totalSize -= 1


            colSize -= 1
            rowSize -= 1
            offset += 1

        return spiral


