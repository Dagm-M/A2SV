testCases = int(input())

for test in range(testCases):
    isNo = False
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    for index in range(1,n):
        if abs(nums[index] - nums[index - 1]) > 1:
            print('NO')
            isNo = True
    if not isNo:
        print('YES')
    

