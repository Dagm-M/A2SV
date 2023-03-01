class Solution:
    def evaluate(self,a,b,oprand):
        if oprand == "+":
            return b + a
        if oprand == "-":
            return b - a
        if oprand == "*":
            return b * a
        if oprand == "/":
            return int(b / a)

    def check(self,a):
        if "-" in a:
            return a[1:].isdigit()
        else:
            return a.isdigit()

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if self.check(token):
                stack.append(int(token))
            else:
                stack.append(self.evaluate(stack.pop(),stack.pop(),token))

        return stack[0]
