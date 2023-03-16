class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        ans = inf
        cookies.sort(reverse = True)

        def distribute(sums,curr):
            nonlocal ans
            if curr >= n:
                ans = min(ans,max(sums))
                return

            for i in range(k):
                if sums[i] + cookies[curr] < ans:
                    sums[i] += cookies[curr]
                    distribute(sums,curr+1)
                    sums[i] -= cookies[curr]

        distribute([0]*k,0)

        return ans
