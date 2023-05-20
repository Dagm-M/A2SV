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
        if xrep <= yrep:
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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        ans = []
        for i in range(len(s1)):
            uf.union(ord(s1[i]) - 97, ord(s2[i]) - 97)

        for i in range(26):
            uf.representative(i)

        for char in baseStr:
            temp = uf.representative(ord(char)-97)
            ans.append(chr(temp + 97))

        return "".join(ans)