class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageToScore = []
        memo = defaultdict(int)

        for i in range(len(scores)):
            ageToScore.append([ages[i],scores[i]])

        ageToScore.sort()

        dp = [0] * len(scores)

        for i in range(len(scores)):
            curr = ageToScore[i][1]
            dp[i] = curr

            for j in range(i):
                if ageToScore[j][1] <= curr:
                    dp[i] = max(dp[i], curr + dp[j])

        return max(dp)
