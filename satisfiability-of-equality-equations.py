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
        if x not in self.rep:
            self.rep[x] = x
        if y not in self.rep:
            self.rep[y] = y
        xrep = self.representative(x)
        yrep = self.representative(y)
        if self.rank[xrep] >= self.rank[yrep]:
            self.rep[yrep] = xrep
            if self.rank[xrep] == self.rank[yrep]:
                self.rank[xrep] += 1
        else:
            self.rep[xrep] = yrep
                

    def connected(self, x, y):
        if x not in self.rep or y not in self.rep:
            return False

        return self.rep[x] == self.rep[y]

    def res(self):
        return self.rep


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()

        for equation in equations:
            if not uf.connected(equation[0], equation[-1]) and equation[1] == "=":
                uf.union(equation[0], equation[-1])

        for equation in equations:
            uf.representative(equation[0])
            uf.representative(equation[-1])
            if uf.connected(equation[0], equation[-1]):
                if equation[1] == "!":
                    return False
            elif equation[0] == equation[-1] and equation[1] == "!":
                return False

        return True