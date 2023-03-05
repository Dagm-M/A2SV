class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        monoStack = []
        seen = set()
        count = Counter(s)
        

        for char in s:

            while len(monoStack) != 0 and ord(char) < ord(monoStack[-1]) and count[monoStack[-1]] > 0 and char not in seen:
                seen.remove(monoStack[-1])
                monoStack.pop()
            
            if char not in seen:
                monoStack.append(char)
                seen.add(char)

            count[char] -= 1


        return "".join(monoStack)
