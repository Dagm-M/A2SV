class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0] * (len(nums) + 1)
        nums.sort(reverse=True)
        total = 0

        for start,end in requests:
            arr[start] += 1
            arr[end + 1] -= 1

        for i in range(1,len(arr)):
            arr[i] += arr[i-1]

        arr.sort(reverse=True)

        for i in range(len(nums)):
            if arr[i] == 0:
                break
            total += nums[i] * arr[i]

        return total % (pow(10,9) + 7)
