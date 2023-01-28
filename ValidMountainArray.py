class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left = 1
        right = len(arr) - 2

        if len(arr) < 3:
            return False

        while left < len(arr):
            if arr[left - 1] >= arr[left]:
                break
            left += 1

        while right >= 0 :
            if arr[right + 1] >= arr[right]:
                break
            right -= 1

        if left - 1 == right + 1 and left - 1 != 0 and right + 1 != len(arr) - 1:
            return True
        
        return False
