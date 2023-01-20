class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        wordsCount = []

        for i in range(ord('a'), ord('z') + 1):
            char = chr(i)
            temp = []

            for word in words:
                count = word.count(char)
                temp.append(count)

            wordsCount.extend([char] * min(temp))

        

        return wordsCount
