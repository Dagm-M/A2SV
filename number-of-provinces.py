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
        return self.rep[x] == self.rep[y]

    def res(self):
        return self.rep

class Solution(object):
    def findCircleNum(self, isConnected):
        uf = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] != 0:
                    uf.union(i,j)
        for i in range(len(isConnected)):
            uf.representative(i)
        res = uf.res()
        count = set()
        for val in res.values():
            count.add(val)

        return len(count)