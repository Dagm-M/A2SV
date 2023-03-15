class Solution:
    def search(self,intervals,num):
        left = 0
        right = len(intervals) - 1

        while left <= right:
            mid = left + (right - left)//2

            if intervals[mid][0] == num:
                return mid
            elif intervals[mid][0] < num:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans = [0] * n
        for i in range(n):
            intervals[i].append(i)

        intervals.sort()
        for i in range(n):
            index = self.search(intervals,intervals[i][1])
            if index >= n:
                ans[intervals[i][2]] = -1
            else:
                ans[intervals[i][2]] = intervals[index][2]

        return ans
