class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]

        total = 0

        def merge(left, right):
            nonlocal total
            p1 = 0
            p2 = 0
            arr = []
            n = len(left)
            m = len(right)

            while p1 < n and p2 < m:
                if left[p1] <= right[p2] + diff:
                    total += m - p2
                    p1 += 1
                else:
                    p2 += 1

            left.append(inf)
            right.append(inf)
            p1 = 0
            p2 = 0

            while p1 < n or p2 < m:
                if left[p1] <= right[p2]:
                    arr.append(left[p1])
                    p1 += 1
                else:
                    arr.append(right[p2])
                    p2 += 1

            return arr

        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr)//2

            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left,right)

        mergeSort(nums1)

        return total
