class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        largest = pow(2,31) - 1

        for i in range(32):
            counter = 0
            for num in nums:
                if (1 << i) & num != 0:
                    counter += 1

            if counter % 3 != 0:
                res = res ^ (1 << i)

        if res > largest:
            res -= pow(2,32)
        return res
