class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = {"1":1, '2':2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
        firstNum = 0
        secondNum = 0
        multiplayer = 1

        index = len(num1) - 1
        while index >= 0:
            firstNum += nums[num1[index]] * multiplayer
            multiplayer *= 10
            index -= 1

        multiplayer = 1

        index = len(num2) - 1
        while index >= 0:
            secondNum += nums[num2[index]] * multiplayer
            multiplayer *= 10
            index -= 1

        return str(firstNum * secondNum)
