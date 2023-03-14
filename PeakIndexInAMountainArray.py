class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n - 1
        pick = 0

        while left <= right:
            mid = left + (right - left)//2

            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                pick = mid
                right = mid - 1

        return pick
