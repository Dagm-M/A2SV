class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        count = defaultdict(int)

        def primeFactorize(num):
            i = 2
            while num > 1:
                while num % i == 0:
                    num /= i
                    count[i] += 1
                i += 1

        for num in nums:
            primeFactorize(num)

        return len(count)
