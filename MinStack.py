class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min[-1]:
                self.min.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        if self.min:
            return self.min[-1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
