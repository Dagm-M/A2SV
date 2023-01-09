class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        posetive = []
        negative = []
        rearranged = []

        for num in nums:
            if num > 0:
                posetive.append(num)
            else:
                negative.append(num)

        for index in range(len(posetive)):
            rearranged.append(posetive[index])
            rearranged.append(negative[index])

        return rearranged
