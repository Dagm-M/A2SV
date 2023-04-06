from collections import Counter, defaultdict


n, m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append(list(map(str, input())))

for i in range(n):
    count = Counter(matrix[i])
    for j in range(m):
        if count[matrix[i][j]] > 1:
            matrix[i][j] = [matrix[i][j], 1]
        else:
            matrix[i][j] = [matrix[i][j], 0]


for i in range(m):
    count = defaultdict(int)
    for j in range(n):
        count[matrix[j][i][0]] += 1

    for j in range(n):
        if count[matrix[j][i][0]] > 1:
            matrix[j][i][1] = 1

ans = []
for i in range(n):
    for j in range(m):
        if matrix[i][j][1] == 0:
            ans.append(matrix[i][j][0])

print("".join(ans))
