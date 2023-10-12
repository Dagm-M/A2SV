# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        left = 0
        right = n-1
        firstMax = 0

        while left < right:
            mid = left + (right - left) // 2
            prev = mountain_arr.get(mid - 1)
            temp = mountain_arr.get(mid)
            nxt = mountain_arr.get(mid + 1)
            if prev < temp < nxt:
                left = mid
            elif prev > temp > nxt:
                right = mid
            else:
                firstMax = mid
                break


        def binarySearch(t,end):
            left = 0
            right = end

            while left <= right:
                mid = left + (right - left) // 2
                temp = mountain_arr.get(mid)
                if target > temp:
                    left = mid + 1
                elif target < temp:
                    right = mid - 1
                else:
                    return mid

            return -1

        def binarySearch1(t,start,end):
            left = start
            right = end

            while left >= right:
                mid = left + (right - left) // 2
                temp = mountain_arr.get(mid)
                if target > temp:
                    left = mid - 1
                elif target < temp:
                    right = mid + 1
                else:
                    return mid

            return -1

        temp = binarySearch(target, firstMax)
        if temp == -1:
            return binarySearch1(target, n-1, firstMax)


        return temp
