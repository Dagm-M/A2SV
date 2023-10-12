class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            gas[i] -= cost[i]

        larg = gas[n-1]
        idx = n-1

        for i in range(len(gas) - 2, -1, -1):
            gas[i] += gas[i+1]
            if gas[i] > larg:
                larg = gas[i]
                idx = i

        if gas[0] < 0:
            return -1
        else:
            return idx
