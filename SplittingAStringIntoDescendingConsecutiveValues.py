class Solution:
    def splitString(self, s: str) -> bool:
        arr = []

        def split(pos):
            if len(s) <= pos:
                return len(arr) >= 2

            for i in range(pos,len(s)):
                num = int(s[pos:i+1])
                if len(arr) == 0 or arr[-1] - num == 1:
                    arr.append(num)
                    if split(i+1):
                        return True
                    arr.pop()

            return False

        return split(0)
