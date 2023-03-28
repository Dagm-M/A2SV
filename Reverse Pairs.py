class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        total = 0

        def merge(left, right):
            nonlocal total
            arr = []
            n = len(left)
            m = len(right)
            p1 = n-1
            p2 = m-1

            while p1 >= 0 and p2 >= 0:
                if left[p1] > right[p2] * 2:
                    total += p2 + 1
                    p1 -= 1
                else:
                    p2 -= 1

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

        mergeSort(nums)

        return total
