# Enter your code here. Read input from STDIN. Print output to STDOUT
set1Size = int(input())
set1 = set(input().split())

set2Size = int(input())
set2 = set(input().split())

print(len(set1 - set2))
