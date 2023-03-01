class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        sum = 0
        curr = 1
        isPush = True

        for char in s:
            if char == "(":
                stack.append("(")
                curr *= 2
                isPush = True
            else:
                if isPush:
                    sum += (curr//2)
                curr = curr//2
                stack.pop()
                isPush = False

        return sum
