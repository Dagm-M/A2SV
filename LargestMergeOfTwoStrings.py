class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr1 = 0
        ptr2 = 0
        word3 = []

        word1 = list(map(str,word1))
        word2 = list(map(str, word2))

        n = len(word1)
        m = len(word2)
        word1.append("A")
        word2.append("B")

        while ptr1 < n or ptr2 < m:
            if word1[ptr1] > word2[ptr2]:
                word3.append(word1[ptr1])
                ptr1 += 1
            elif word1[ptr1] < word2[ptr2]:
                word3.append(word2[ptr2])
                ptr2 += 1
            else:
                inc = 1
                while True:
                    if word1[ptr1 + inc] > word2[ptr2 + inc]:
                        word3.append(word1[ptr1])
                        ptr1 += 1
                        break
                    elif word1[ptr1 + inc] < word2[ptr2 + inc]:
                        word3.append(word2[ptr2])
                        ptr2 += 1
                        break
                    
                    inc += 1

        return "".join(word3)
