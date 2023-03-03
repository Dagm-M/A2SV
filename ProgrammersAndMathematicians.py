testCases = int(input())

for i in range(testCases):
    p, m = map(int, input().split())

    groups = (p+m)//4

    answer = min(groups, p, m)
    print(answer)
=
