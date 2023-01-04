class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = []
        MOD = pow(10, 9) + 7
        countOfDeliciousness = Counter(deliciousness)
        goodMeals = set()

        for i in range(22):
            powers.append(2**i)

        for delicious in countOfDeliciousness.keys():
            for power in powers:
                if power - delicious in countOfDeliciousness and \
                    (delicious != power - delicious or countOfDeliciousness[power - delicious] > 1) and \
                    (power - delicious, delicious) not in goodMeals:

                    goodMeals.add((delicious, power - delicious))

        mealSum = 0
        for m in goodMeals:
            if m[0] == m[1]:
                mealSum += ((countOfDeliciousness[m[0]] - 1)
                        * (countOfDeliciousness[m[0]]) // 2)
            else:
                mealSum += (countOfDeliciousness[m[0]]
                        * countOfDeliciousness[m[1]])

        return int(mealSum % MOD)
