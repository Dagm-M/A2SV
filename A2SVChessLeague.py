from cmath import inf
n, k = map(int, input().split())
nums = list(map(int, input().split()))
arr = []
for i in range(1, pow(2, n)+1):
    arr.append(i)
 
 
def winners(arr, nums, k):
    if len(arr) == 1:
        return arr
 
    size = int(len(arr)/2)
 
    left = winners(arr[:size], nums, k)
    right = winners(arr[size:], nums, k)
    ans = []
 
    minL = inf
    minR = inf
    for i in left:
        minL = min(minL, nums[i-1])
 
    for i in right:
        minR = min(minR, nums[i-1])
 
    for i in left:
        if nums[i-1] > minR:
            ans.append(i)
        elif abs(nums[i-1] - minR) <= k:
            ans.append(i)
 
    for j in right:
        if nums[j-1] > minL:
            ans.append(j)
        elif abs(nums[j-1] - minL) <= k:
            ans.append(j)
 
    return ans
 
 
print(*winners(arr, nums, k))
