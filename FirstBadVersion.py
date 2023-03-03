# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        mid = 0
        temp = 0


        while left <= right:
            mid = (right + left)//2

            if isBadVersion(mid):
                right = mid - 1
                temp = mid
            else:
                left = mid + 1


        return temp
