class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        finalWord = []

        for index in range(max(len(word1),len(word2))):
            if(len(word1) > index):
                finalWord.append(word1[index])
            if(len(word2) > index):
                finalWord.append(word2[index])
        
        return "".join(finalWord)
