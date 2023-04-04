class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        first = c[deck[0]]

        def GCD(a,b):
            if b == 0:
                return a
        
            return GCD(b, a%b)

        for value in c.values():
            if first != value:
                temp = GCD(first,value)
                if temp == 1:
                    return False
                first = temp
            elif value == 1:
                return False

        return True
