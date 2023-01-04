class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matchWonAndLost = defaultdict(list)
        notLost = []
        lostOnce = []

        for match in matches:
            if len(matchWonAndLost[match[0]]) == 0:
                matchWonAndLost[match[0]].append(0)
                matchWonAndLost[match[0]].append(0)

            matchWonAndLost[match[0]][0] += 1

            if len(matchWonAndLost[match[1]]) == 0:
                matchWonAndLost[match[1]].append(0)
                matchWonAndLost[match[1]].append(0)

            matchWonAndLost[match[1]][1] += 1

        for key,value in matchWonAndLost.items():
            if value[1] == 0:
                notLost.append(key)
            if value[1] == 1:
                lostOnce.append(key)

        notLost.sort()
        lostOnce.sort()

        return [notLost, lostOnce]
