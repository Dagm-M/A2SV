# Enter your code here. Read input from STDIN. Print output to STDOUT
numOfTest = int(input())
sizeOfEach = []
lists = []
for i in range(numOfTest):
    sizeOfEach.append(int(input()))
    lists.append([int(item) for item in input().split()])

for x in lists:
    left, right = 0, len(x)-1
    isNo = False
    bottom = max(x[left],x[right])
    
    while left <= right:
        if x[left] > bottom or x[right] > bottom:
            print('No')
            isNo = True
            break
        elif x[left] > x[right]:
            bottom = x[left]
            left+=1
        else:
            bottom = x[right]
            right-=1
    if not isNo:
        print('Yes')
        
        
        
        
