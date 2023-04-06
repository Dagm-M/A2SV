isodd = False
isEven = False

n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num % 2 == 0:
        isEven = True
    else:
        isodd = True

if isEven and isodd:
    nums.sort()
    print(*nums)
else:
    print(*nums)
