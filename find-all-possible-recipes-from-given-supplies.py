class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        q = deque()
        ans = []

        adj = defaultdict(list)
        indegree = defaultdict(int)

        for supplie in supplies:
            q.append(supplie)

        for i,recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                adj[ingredient].append(recipe)
                indegree[recipe] += 1

        while q:
            val = q.popleft()
            if val in indegree:
                ans.append(val)

            for ad in adj[val]:
                indegree[ad] -= 1
                if indegree[ad] == 0:
                    q.append(ad)

        return ans