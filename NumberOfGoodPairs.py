class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = {}
        counter = 0
        for num in nums:
            if num in goodPairs.keys():
                counter += goodPairs[num]
                goodPairs[num] += 1
            else:
                goodPairs[num] = 1

        return counter
            
