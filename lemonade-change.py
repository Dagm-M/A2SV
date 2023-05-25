class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5 = 0
        bill10 = 0

        for bill in bills:
            if bill == 5:
                bill5 += 1
            elif bill == 10:
                bill10 += 1
                if bill5 < 1:
                    return False
                bill5 -= 1
            else:
                
                if bill10 < 1:
                    if bill5 < 3:
                        return False
                    bill5 -= 3
                else:
                    if bill5 < 1:
                        return False
                    bill10 -= 1
                    bill5 -= 1
                
        return True