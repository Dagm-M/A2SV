class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        largestIndex = {}
        maxPartitions = []
        prev = 0
        firstMin = 0

        for index,char in enumerate(s):
            if char in largestIndex:
                largestIndex[char][1] = index
            else:
                largestIndex[char] = [index,index]

        for a,b in largestIndex.values():
            if prev >= a:
                prev = max(prev,b)
            else:
                maxPartitions.append(prev - firstMin + 1)
                firstMin = a
                prev = b

        maxPartitions.append(prev - firstMin + 1)

        return maxPartitions
        
