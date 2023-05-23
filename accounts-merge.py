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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        seen = set()
        uf = UnionFind()
        ans = defaultdict(list)
        final = []

        for i,account in enumerate(accounts):

            if account[0] in seen:
                account[0] = account[0] + str(i)
            for j in range(len(account)):
                uf.union(account[0], account[j])

            seen.add(account[0])
        
        seen = set()
        for x,account in enumerate(accounts):

            if account[0] in seen:
                account[0] = account[0] + str(x)
            for y in range(len(account)):
                uf.representative(account[0])
                uf.representative(account[y])

            
            seen.add(account[0])
            
        temp = uf.res()

        for key,val in temp.items():
            if key not in seen:
                ans[val].append(key)

        for key, val in ans.items():
            temp = list(key)
            while temp[-1].isnumeric():
                temp.pop()

            temp2 = ["".join(temp)]
            val.sort()
            temp2.extend(val)
            final.append(temp2)


        return final