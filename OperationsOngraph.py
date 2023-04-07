from collections import defaultdict


vertex = int(input())

k = int(input())
edges = defaultdict(list)

for i in range(k):
    nums = list(map(int, input().split()))

    if nums[0] == 1:
        edges[nums[1]].append(nums[2])
        edges[nums[2]].append(nums[1])
    else:
        print(*edges[nums[1]])
