def checkX(row1, col1, matrix, n, m):
    sum = 0
    row = row1
    col = col1
    while 0 <= row < n and 0 <= col < m:
        sum += matrix[row][col]
        col -= 1
        row -= 1
 
    row = row1 + 1
    col = col1 - 1
 
    while 0 <= row < n and 0 <= col < m:
        sum += matrix[row][col]
        col -= 1
        row += 1
 
    row = row1 - 1
    col = col1 + 1
 
    while 0 <= row < n and 0 <= col < m:
        sum += matrix[row][col]
        col += 1
        row -= 1
 
    row = row1 + 1
    col = col1 + 1
 
    while 0 <= row < n and 0 <= col < m:
        sum += matrix[row][col]
        col += 1
        row += 1
 
    return sum
 
 
def main():
    testCases = int(input())
 
    for test in range(testCases):
        n, m = list(map(int, input().split()))
        matrix = []
        Xsum = []
 
        for num in range(n):
            matrix.append(list(map(int, input().split())))
 
        for row in range(n):
            for col in range(m):
                Xsum.append(checkX(row, col, matrix, n, m))
 
        print(max(Xsum))
 
 
main()
