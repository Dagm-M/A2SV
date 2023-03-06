class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        windowL = -inf
        windowR = inf
        tChars = Counter(t)
        counter = len(t)

        for right in range(len(s)):
            if s[right] in tChars:
                if tChars[s[right]] > 0:
                    counter -= 1
                tChars[s[right]] -= 1

            
            while counter <= 0:
                if windowR - windowL > right - left:
                    windowR = right
                    windowL = left

                if s[left] in tChars:
                    tChars[s[left]] += 1
                    if tChars[s[left]] > 0:
                        counter += 1
                left += 1
            
        
        if windowR != inf:
            return s[windowL : windowR + 1]
        else:
            return ""
