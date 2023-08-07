class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0

        visited = [0] * (n+1)

        def calculate(pos):
            nonlocal count
            if pos > n:
                count += 1

            for i in range(1,n + 1):
                if not bool(visited[i]) and (pos % i == 0 or i % pos == 0):
                    visited[i] = 1
                    calculate(pos + 1)
                    visited[i] = 0

        calculate(1)

        return count
