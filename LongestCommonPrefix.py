class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = strs[0]

        for word in strs:
            wasIn = False
            for index in range(min(len(commonPrefix),len(word))):
                if word[index] != commonPrefix[index]:
                    commonPrefix = word[:index]
                    wasIn = True
                    break
            if not wasIn:
                commonPrefix = word if len(commonPrefix) > len(word) else commonPrefix
        
        return commonPrefix
