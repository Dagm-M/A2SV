class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [1 for i in range(n)]
        i = 0
        primes[0] = 0
        primes[1] = 0

        while i * i <= n:
            if primes[i]:
                j = i * i

                while j < n:
                    primes[j] = 0
                    j += i

            i += 1

        return Counter(primes)[1]
