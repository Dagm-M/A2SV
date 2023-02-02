class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        if len(mat) * len(mat[0]) != r * c:
            return mat

        newMat = []
        temp = []

        for row in range(len(mat)):
            for col in range(len(mat[0])):

                temp.append(mat[row][col])

                if len(temp) == c:
                    newMat.append(temp)
                    temp = []

                

        return newMat
        
