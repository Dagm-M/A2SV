    def isVowel(self, c: str) -> bool:
        if c in ['a', 'e', 'i', 'o', 'u']:
            return True
        else:
            return False

    def countVowels(self, word: str) -> int:
        sum = 0
        n = len(word)

        for i in range(n):
            if self.isVowel(word[i]):
                sum += (n - i) * (i + 1)

        return sum
