n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

source = []
sink = []

for i in range(len(matrix[0])):
    isOne = False
    for j in range(len(matrix)):
        if matrix[j][i] == 1:
            isOne = True

    if not isOne:
        source.append(i+1)

for i in range(len(matrix)):
    isOne = False
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            isOne = True

    if not isOne:
        sink.append(i+1)


print(len(source), *source)
print(len(sink), *sink)
