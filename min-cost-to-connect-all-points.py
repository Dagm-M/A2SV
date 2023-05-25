class UnionFind:
    def __init__(self):
        self.rank = defaultdict(int)
        self.rep = defaultdict(str)
        
    def representative(self, x):
        if x not in self.rep:
            self.rep[x] = x
        temp = x
        while self.rep[x] != x:
            x = self.rep[x]
        while self.rep[temp] != temp:
            self.rep[temp] = x
            temp = self.rep[temp]
        return x
		
    def union(self, x, y):
        xrep = self.representative(x)
        yrep = self.representative(y)
        if self.rank[xrep] >= self.rank[yrep]:
            self.rep[yrep] = xrep
            if self.rank[xrep] == self.rank[yrep]:
                self.rank[xrep] += 1
        else:
            self.rep[xrep] = yrep
                

    def connected(self, x, y): 
        self.representative(x)
        self.representative(y)

        return self.rep[x] == self.rep[y]

    def res(self):
        return self.rep

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UnionFind()
        n = len(points)
        arr = []
        total = 0

        def distance(a,b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dist = distance(points[i],points[j])
                arr.append([dist,i,j])
        arr.sort()

        
        for a,b,c in arr:
            if not uf.connected(b,c):
                uf.union(b,c)
                total += a

        return total