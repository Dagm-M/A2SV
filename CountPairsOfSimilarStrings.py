class Solution:
    def similarPairs(self, words: List[str]) -> int:

        for index in range(len(words)):
            new = set(words[index])
            words[index] = new
            

        counter = 0

        for index in range(len(words)):
            for i in range(index+1,len(words)):
                if words[index] == words[i]:
                    counter += 1
        
        return counter
            
