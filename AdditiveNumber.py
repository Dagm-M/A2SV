class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        stack = []

        def isAdditive(pos):
            if pos >= len(num):
                return len(stack) > 2


            for i in range(pos,len(num)):
                temp = num[pos:i+1]
                n = int(temp)
                if len(temp) > 1 and temp[0] == "0":
                    return False
                
                if len(stack) < 2 or stack[-1] + stack[-2] == n:
                    stack.append(n)
                    if isAdditive(i+1):
                        return True
                    stack.pop()

                elif n > stack[-1] + stack[-2]:
                    break

            return False

        return isAdditive(0)

                
