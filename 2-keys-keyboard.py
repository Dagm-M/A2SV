class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        div = 2
        ans = []
        num = n
        while div * div <= n:
            while num % div == 0:
                num //= div
                ans.append(div)
            div += 1

        if num != 1:
            ans.append(num)

        return sum(ans)