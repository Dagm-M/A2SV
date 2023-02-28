class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maximum = 0
        chars = {}
        right = 0
        left = 0

        while right < len(s):
            if s[right] in chars.keys():
                chars[s[right]] += 1
            else:
                chars[s[right]] = 1

            maximum = max(maximum, chars[s[right]])

            if (k + maximum) < (right - left + 1):
                chars[s[left]] -= 1
                left += 1
               
            right += 1

        if maximum + k > len(s):
            return len(s)
        else:
            return maximum + k

        
