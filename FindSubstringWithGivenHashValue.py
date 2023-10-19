class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        hash = 0
        powers = []
        n = len(s)
        for i in range(k):
            powers.append(pow(power, i, modulo))
        i = 0
        while i < k:
            hash += (ord(s[n - k + i]) - 96) * powers[i]
            i += 1

        index = n - k
        for i in range(n-k-1, -1, -1):
            hash -= (ord(s[i + k]) - 96) * powers[k-1]
            hash = hash * power + (ord(s[i]) - 96)
            hash %= modulo
            if hash % modulo == hashValue:
                index = i

        return s[index:index+k]
