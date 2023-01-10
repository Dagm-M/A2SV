class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indexOfOnes = []
        boxes = [*boxes]
        minNumOfOperations = []


        for index,box in enumerate(boxes):
            if box == "1":
                indexOfOnes.append(index)

        for index,box in enumerate(boxes):
            sum = 0
            for i in indexOfOnes:
                sum += abs(i - index)
            minNumOfOperations.append(sum)
            
        return minNumOfOperations
