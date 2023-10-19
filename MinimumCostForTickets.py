class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = defaultdict(int)
        
        def dp(idx,skip):
            if idx >= len(days):
                return 0

            if (idx,skip) in memo:
                return memo[(idx,skip)]

            val = inf
            if skip < days[idx]:
                val = min(dp(idx + 1, days[idx]) + costs[0], val)
                val = min(dp(idx + 1, days[idx] + 6) + costs[1], val)
                val = min(dp(idx + 1, days[idx] + 29) + costs[2], val)
            else:
                val = min(dp(idx + 1, skip), val)


            memo[(idx,skip)] = val

            return memo[(idx,skip)]

        return dp(0,0)
