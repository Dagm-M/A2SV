class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left = 0
        maxFruits = 1
        n = len(fruits)
        seen = defaultdict(int)

        for right in range(n):

            seen[fruits[right]] += 1

            while left <= right and len(seen) > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]

                left += 1
            
            maxFruits = max(maxFruits, right - left + 1)

        return maxFruits
