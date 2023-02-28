class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        change = [0] * (len(s) + 1)

        for shift in shifts:
            if shift[2] != 0:
                change[shift[0]] += 1
                change[shift[1] + 1] -= 1
            else:
                change[shift[0]] -= 1
                change[shift[1] + 1] += 1    

        for i in range(1,len(change)):
            change[i] += change[i-1]

        s = list(map(str,s))

        for i in range(len(s)):

            # make change below 26
            change[i] = change[i] % 26
            val = ord(s[i]) + change[i]

            # if greater than z or less then a loop back
            if val > 122:
                s[i] = chr(96 + (val - 122))
            elif ord(s[i]) + change[i] < 97:
                s[i] = chr(123 - (val + 97))
            else:
                s[i] = chr(val)
        
        return "".join(s)         
