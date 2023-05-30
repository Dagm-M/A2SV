class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)
        def tribona(t):
            if t == 0:
                return 0
            if t == 1 or t == 2:
                return 1
            
            if t not in memo:
                memo[t] = tribona(t-3) + tribona(t-2) + tribona(t-1)

            return memo[t]

        return tribona(n)