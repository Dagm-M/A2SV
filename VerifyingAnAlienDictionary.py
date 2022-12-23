class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderByNumber = {}

        for index,char in enumerate(order):
            orderByNumber[char] = index

        currentOrder = words[0]

        for word in words:
            isGreater = True
            for index in range(min(len(word), len(currentOrder))):
                if orderByNumber.get(currentOrder[index]) > orderByNumber.get(word[index]):
                    return False
                elif orderByNumber.get(currentOrder[index]) < orderByNumber.get(word[index]):
                    isGreater = False
                    break


            if(len(currentOrder) > len(word) and isGreater):
                return False
            
            currentOrder = word

            
        return True
