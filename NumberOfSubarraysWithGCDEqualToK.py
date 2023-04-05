class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        def GCD(a,b):
            if b == 0:
                return a

            return GCD(b, a % b)


        for i in range(len(nums)):
            gcd = nums[i]
            for j in range(i,len(nums)):
                gcd = GCD(gcd,nums[j])
                if gcd == k:
                    count += 1


        return count
