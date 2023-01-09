class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string = []

        for char in s:
            string.append(char)

        spaces.sort()
        indexOfSpace = 0
        newString = []

        for index,char in enumerate(string):

            if len(spaces) > indexOfSpace and index == spaces[indexOfSpace]:
                newString.append(" ")
                indexOfSpace += 1

            newString.append(char)

        return "".join(newString)
