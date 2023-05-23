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
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        ans = set()

        for i,[a,b] in enumerate(stones):
            uf.union(chr(97+i), a)
            uf.union(chr(97+i), str(b))

        for i,[a,b] in enumerate(stones):
            uf.representative(a)
            uf.representative(str(b))
            uf.representative(chr(97+i))

        temp = uf.res()

        for key,val in temp.items():
            ans.add(val)

        return len(stones) - len(ans)