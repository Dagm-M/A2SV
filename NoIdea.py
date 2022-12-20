# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input()
n = int(size[0])
m = int(size[2])
l = input().split()
A = set(input().split())
B = set(input().split())
happy = 0


for i in l:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1
    
print(happy)
