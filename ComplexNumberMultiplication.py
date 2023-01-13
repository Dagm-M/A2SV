class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = list(map(int,num1[:-1].split("+")))
        num2 = list(map(int,num2[:-1].split("+")))

        num3 = str((num1[0] * num2[0]) - (num1[1] * num2[1])) + "+" + str((num1[0] * num2[1]) + (num1[1] * num2[0])) + "i"
        
        
        return num3
