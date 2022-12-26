class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()

        for index in range(len(s)):
            if s[index] != t[index]:
                return t[index]
        
        return t.pop()
        
