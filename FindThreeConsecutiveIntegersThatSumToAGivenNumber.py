class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            num = num//3
            return [num-1, num , num+1]
        else:
            return []
