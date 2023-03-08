class Solution:
    def extractNum(self,s,start):
        num = []
        for i in range(start,len(s)):
            if s[i] == "[":
                break
            num.append(s[i])

        return [i,int("".join(num))]

    def extractStr(self,s,start):
        string = []
        count = 0
        for i in range(start,len(s)):
            if s[i] == "[":
                count += 1
            if s[i] == "]":
                if count == 0:
                    break
                count -= 1
            string.append(s[i])

        return [i, "".join(string)]

    def decodeString(self, s: str) -> str:
        if s.isdigit():
            return ""

        isClear = True
        for c in s:
            if c.isdigit() or "[" == c or "]" == c:
                isClear = False
        if isClear:
            return s

        

        if s[0].isdigit():
            i,num = self.extractNum(s,0)
            i,string = self.extractStr(s,i+1)
            
            while i < len(s) and s[i] == "]":
                i += 1

            temp = (num * self.decodeString(string)) + self.decodeString(s[i:])
            return temp

        else:
            i = 0
            while not s[i].isdigit():
                i += 1
            
            return s[:i] + self.decodeString(s[i:])

