n = int(input())
ans = 0

for i in range(n):
    nums = list(map(int, input().split()))
    ans += nums[i:].count(1)

print(ans)
