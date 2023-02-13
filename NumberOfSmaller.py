n, m = map(int, input().split())

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

ptr1 = 0
ptr2 = 0
numLess = []
lessCount = 0

while ptr1 < len(nums1) and ptr2 < len(nums2):

    while ptr1 < len(nums1) and nums1[ptr1] < nums2[ptr2]:
        lessCount += 1
        ptr1 += 1

    numLess.append(lessCount)
    ptr2 += 1

while ptr2 < len(nums2):
    numLess.append(lessCount)
    ptr2 += 1

print(*(numLess))
