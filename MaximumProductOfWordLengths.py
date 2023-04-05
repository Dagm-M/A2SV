class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def setBit(num, k):
            num |= (1 << k)
            return num

        binary = []
        maxVal = 0

        for word in words:
            temp = 0
            for char in word:
                temp = setBit(temp,ord(char) - 97)

            binary.append(temp)

        for i in range(len(binary)):
            for j in range(i,len(binary)):
                if binary[i] & binary[j] == 0:
                    prod = len(words[i]) * len(words[j])
                    maxVal = max(maxVal, prod)

        return maxVal
