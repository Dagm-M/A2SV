class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        memo = defaultdict(int)
        n = len(matrix)
        ans = inf

        def minPathSum(row, col):
            nonlocal n
            if row >= n:
                return 0
            if col >= n or col < 0:
                return 10000

            if (row,col) not in memo:
                memo[(row,col)] = min(minPathSum(row+1, col -1) + matrix[row][col], minPathSum(row+1, col) + matrix[row][col], minPathSum(row+1, col + 1) + matrix[row][col])

            return memo[(row,col)]

        for i in range(n):
            ans = min(ans, minPathSum(0, i))

        return ans
