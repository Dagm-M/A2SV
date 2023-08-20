class Solution:
    def numTrees(self, n: int) -> int:
        memo = defaultdict(int)

        def numTree(i):
            if i <= 1:
                return 1

            if i not in memo:
                for j in range(1, i+1):
                    memo[i] += numTree(j-1) * numTree(i-j)

            return memo[i]

        return numTree(n)
