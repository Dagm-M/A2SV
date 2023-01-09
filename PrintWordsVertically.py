class Solution:
    def printVertically(self, s: str) -> List[str]:

        words = s.split()
        maxWordSize = 1
        vertical = []
        index = 0

        while index < maxWordSize:
            temp = []

            for word in words:
                maxWordSize = max(maxWordSize, len(word))
                if len(word) > index:
                    temp.append(word[index])
                else:
                    temp.append(" ")

            vertical.append("".join(temp).rstrip())

            index += 1
        
        return vertical
