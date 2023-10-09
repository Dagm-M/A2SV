class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        prev, curr = 0, 1
        lps = [0 for i in range(len(needle))]
        while curr < len(needle):
            if needle[curr] == needle[prev]:
                lps[curr] = prev + 1
                prev += 1
                curr += 1
            elif prev == 0:
                curr += 1
            else:
                prev = lps[prev-1]

        i, j = 0, 0
        
        while i < len(haystack):
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            elif j == 0:
                i += 1  
            else:
                j = lps[j-1]

            if j == len(needle):
                return i - j
        
        return -1
