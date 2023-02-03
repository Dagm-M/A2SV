class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        visited = set()

        for row in range(n):
            for col in range(n):
                if (row,col) not in visited:

                    temp = matrix[col][n-row-1]
                    matrix[col][n-row-1] = matrix[row][col]
                    visited.add((row,col))

                    temp, matrix[n-row-1][n-col-1] = matrix[n-row-1][n-col-1], temp
                    visited.add((col,n-row-1))

                    temp, matrix[n-col-1][row] = matrix[n-col-1][row], temp
                    visited.add((n-row-1,n-col-1))

                    matrix[row][col] = temp
                    visited.add((n-col-1,row))

                    
