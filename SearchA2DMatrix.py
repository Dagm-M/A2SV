class Solution:
    def binarySearchCol(self,matrix,target):
        left = 0
        right = len(matrix) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return [mid,right]

        return [left,right]

    def binarySearchRow(self,row,target):
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = (left + right) // 2
            if row[mid] < target:
                left = mid + 1
            elif row[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left,right = self.binarySearchCol(matrix,target)
        if left >= 0 and left < len(matrix):
            row = matrix[left]
            index = self.binarySearchRow(row,target)
            if index >= 0:
                return True

        if right >= 0 and right < len(matrix):
            row = matrix[right]
            index = self.binarySearchRow(row,target)
            if index >= 0:
                return True

        
        return False
