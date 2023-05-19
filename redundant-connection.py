class UnionFind:
    def __init__(self, size):
        self.rank = defaultdict(int)
        self.rep = {i:i for i in range(size)}
        
    def representative(self, x):
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        ans = [0,0]
        for a,b in edges:
            if uf.connected(a-1,b-1):
                ans[0] = a
                ans[1] = b

            uf.union(a-1,b-1)

        return ans