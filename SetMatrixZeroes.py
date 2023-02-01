class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colZero = set()
        for row in range(len(matrix)):
            allRow = False
            for col in range(len(matrix[0])):
                val = matrix[row][col]
                if val == 0:
                    allRow = True
                    colZero.add(col)
                elif col in colZero:
                    matrix[row][col] = 0

            if allRow:
                matrix[row] = [0] * len(matrix[row])

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col in colZero:
                    matrix[row][col] = 0
                    
