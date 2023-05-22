class UnionFind:
    def __init__(self):
        self.rank = defaultdict(int)
        self.rep = defaultdict(str)
        self.minRoad = defaultdict(int)
        
    def representative(self, x):
        if x not in self.rep:
            self.rep[x] = x
            self.minRoad[x] = 10001
        temp = x
        while self.rep[x] != x:
            x = self.rep[x]
        while self.rep[temp] != temp:
            self.rep[temp] = x
            temp = self.rep[temp]
        return x
		
    def union(self, x, y, z):
        xrep = self.representative(x)
        yrep = self.representative(y)
        if self.rank[xrep] >= self.rank[yrep]:
            self.rep[yrep] = xrep
            self.minRoad[xrep] = min(self.minRoad[xrep], self.minRoad[yrep])
            self.minRoad[xrep] = min(self.minRoad[xrep], z)
            if self.rank[xrep] == self.rank[yrep]:
                self.rank[xrep] += 1
        else:
            self.rep[xrep] = yrep
            self.minRoad[yrep] = min(self.minRoad[xrep], self.minRoad[yrep])
            self.minRoad[yrep] = min(self.minRoad[yrep], z)
                

    def connected(self, x, y): 
        self.representative(x)
        self.representative(y)

        return self.rep[x] == self.rep[y]

    def res(self,x):
        x = self.representative(x)
        return self.minRoad[x]

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind()
        for a,b,c in roads:
            uf.union(a,b,c)

        return uf.res(1)