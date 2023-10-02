class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        temp = []
        ans = 0
        for i,a in enumerate(costs):
            temp.append([a[0]-a[1], i])

        temp.sort()

        for j in range(len(costs)//2):
            ans += costs[temp[j][1]][0]
        
        for j in range(len(costs)//2, len(costs)):
            ans += costs[temp[j][1]][1]

        return ans
