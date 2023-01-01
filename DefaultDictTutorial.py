# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

m, n = map(int, input().split())
d = defaultdict(list)

for index in range(m):
    d[input()].append(str(index + 1))
    
for index in range(n):
    found = d[input()]
    if found:
        print(" ".join(found))
    else:
        print("-1")


    
