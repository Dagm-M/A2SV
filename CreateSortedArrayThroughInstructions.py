class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        total = 0
        mod = pow(10,9) + 7
        sortInst = []
        for i,inst in enumerate(instructions):
            bisect.insort(sortInst,inst)
            place = bisect_right(sortInst,inst)
            larger = len(sortInst) - place
            smaller = bisect_right(sortInst,inst-1)
            total += min(smaller,larger)
            total %= mod


        return total
