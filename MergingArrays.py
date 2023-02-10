n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.append(float("inf"))
arr2.append(float("inf"))

ptr1 = 0
ptr2 = 0
merged = []

while ptr1 < n or ptr2 < m:
    if arr1[ptr1] > arr2[ptr2]:
        merged.append(arr2[ptr2])
        ptr2 += 1
    else:
        merged.append(arr1[ptr1])
        ptr1 += 1

print(*(merged))
