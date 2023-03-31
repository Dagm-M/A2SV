class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ (pow(2,num.bit_length())-1)
