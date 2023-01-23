class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        matrix = []
        matrix2 = []

        for col in grid:
            temp = []
            for index in range(3,len(col) + 1):
                temp.append(max(col[index -3: index]))
            
            matrix.append(temp)

        for index in range(len(matrix[0])):
            temp = []
            for col in  matrix:
                temp.append(col[index])

            matrix2.append(temp)

        matrix = []

        for col in matrix2:
            temp = []
            for index in range(3,len(col) + 1):
                temp.append(max(col[index -3: index]))
            
            matrix.append(temp)

        matrix2 = []

        for index in range(len(matrix[0])):
            temp = []
            for col in  matrix:
                temp.append(col[index])

            matrix2.append(temp)

        return matrix2
