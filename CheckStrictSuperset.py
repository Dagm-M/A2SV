# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(input().split())
setSize = int(input())
sets = []

for index in range(setSize):
    sets.append(set(input().split()))
    
for s in sets:
    if s == setA or len(s - setA) != 0:
        print(False)
        exit()
        
print(True)
