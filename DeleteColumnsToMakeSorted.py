class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0

        for index in range(len(strs[0])):
            isSorted = True
            for i in range(len(strs) - 1):
                if ord(strs[i][index]) > ord(strs[i + 1][index]):
                    isSorted = False
                
            if not isSorted:
                counter += 1
                
        return counter
