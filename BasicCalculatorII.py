class Solution:
    def priority(self, a, b):
        if (a in ['*', '/']) and (b in ['*', '/']):
            return False
        if (a in ['+', '-']) and (b in ['+', '-']):
            return True
        if (a in ['/', '*']) and (b in ['+', '-']):
            return False
        else:
            return True

    def compute(self, c, a, b):
        if c == '+':
            return str(a + b)
        if c == '-':
            return str(a - b)
        if c == '*':
            return str(a * b)
        if c == '/':
            return str(a // b)
        return "1"

    def calculate(self, s: str) -> int:
        m = s[0]
        num = [m]
        oper = []
        n = len(s)
        isnum = True

        for i in range(1, n):
            if s[i] == ' ':
                continue
            if s[i] in ['*', '/', '+', '-']:
                if oper:
                    if self.priority(oper[-1], s[i]):
                        oper.append(s[i])
                    else:
                        a = int(num.pop())
                        b = int(num.pop())
                        num.append(self.compute(oper.pop(), b, a))
                        oper.append(s[i])
                else:
                    oper.append(s[i])
                isnum = False

            else:
                if isnum:
                    m = s[i]
                    m = num[-1] + m
                    num[-1] = m
                else:
                    m = s[i]
                    num.append(m)
                isnum = True

        if len(num) != 1 and (oper[-1] in ['*', '/']):
            a = int(num.pop())
            b = int(num.pop())
            num.append(self.compute(oper.pop(), b, a))

        num.reverse()
        oper.reverse()

        while len(num) != 1:
            a = int(num.pop())
            b = int(num.pop())
            num.append(self.compute(oper.pop(), a, b))

        return int(num[0])
