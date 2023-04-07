from collections import defaultdict


n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

adjecent = defaultdict(list)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            adjecent[i+1].append(j+1)

for value in adjecent.values():
    print(len(value), *value)
