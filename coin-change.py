class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)
        coins.sort(reverse = True)
        q = deque()

        if amount == 0:
            return 0

        for coin in coins:
            temp = amount - coin
            if temp >= 0:
                q.append((temp,1))

        while q:
            val = q.popleft()
            memo[val[0]] = val[1]
            if val[0] == 0:
                return val[1]

            for coin in coins:
                temp = val[0] - coin
                if temp >= 0 and temp not in memo:
                    q.append((temp,val[1] + 1))
                    memo[temp] = val[1] + 1
        
        return -1