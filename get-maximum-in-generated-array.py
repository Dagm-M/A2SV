class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n+1)
        nums[1] = 1
        
        def getMaximum(n):
            if n == 0:
                return 0
            if n == 1:
                return 1

            if n % 2 == 0:
                if nums[n] == 0:
                    nums[n] = getMaximum(n//2)
                return nums[n]

            else:
                temp = (n-1)//2
                if nums[n] == 0:
                    nums[n] = getMaximum(temp) + getMaximum(temp + 1)

                return nums[n]

        for i in range(2,n+1):
            getMaximum(i)


        return max(nums)