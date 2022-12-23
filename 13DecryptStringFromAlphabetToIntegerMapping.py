class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        mapping = {}
        s = s[::-1]

        for num in range(26):
            mapping[num + 1] = chr(97 + num)

        i = 0
        while i < len(s):
            if s[i].isdigit():
                stack.append(mapping.get(int(s[i])))
            else:
                num = s[i+ 2] + s[i+1]
                stack.append(mapping.get(int(num)))
                i += 2
            i += 1

        stack.reverse()
        
        return "".join(stack)

            
            
