class Solution:
    def numTeams(self, rating: List[int]) -> int:
        memo = defaultdict(int)

        def dp(index,level,prev):
            if (index,level) in memo:
                return memo[(index,level)]
            if level == 0:
                return 1
            if index < 0 :
                return 0

            count = 0
            for i in range(index):
                if rating[i] > prev:
                    count += dp(i,level -1 ,rating[i])
            memo[(index,level)] = count
            return count

        inc = dp(len(rating),3,-inf)
        rating = rating[::-1]
        memo = defaultdict(int)
        dec = dp(len(rating),3,-inf)
        return inc  + dec
