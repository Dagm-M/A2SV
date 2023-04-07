class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def prime_sieve(n) -> list[bool]:
            is_prime: list[bool] = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2
            while i <= n:
                if is_prime[i]:
                    j = 2 * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return is_prime
        
        prime = prime_sieve(right)
        temp = []
        ans = [-1,-1]
        prev = right+1

        for i in range(left,len(prime)):
            if prime[i]:
                temp.append(i)

        for i in range(1,len(temp)):
            if temp[i] - temp[i-1] < prev:
                ans[0] = temp[i-1]
                ans[1] = temp[i]
                prev = temp[i] - temp[i-1]

        return ans
