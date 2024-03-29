class MyCircularDeque:
    size = 0
    temp = 0
    qu = deque()
    def __init__(self, k: int):
        self.size = k
        self.qu = deque()

    def insertFront(self, value: int) -> bool:
        if self.temp == self.size:
            return False
        self.qu.appendleft(value)
        self.temp += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.temp == self.size:
            return False
        self.temp += 1
        self.qu.append(value)
        return True        

    def deleteFront(self) -> bool:
        if self.temp == 0:
            return False
        self.temp -= 1
        self.qu.popleft()
        return True
    def deleteLast(self) -> bool:
        if self.temp == 0:
            return False
        self.temp -= 1
        self.qu.pop()
        return True

    def getFront(self) -> int:
        if self.temp == 0:
            return -1
        return self.qu[0]

    def getRear(self) -> int:
        if self.temp == 0:
            return -1
        return self.qu[-1]

    def isEmpty(self) -> bool:
        if self.temp == 0:
            return True
        return False        

    def isFull(self) -> bool:
        if self.temp == self.size:
            return True
        return False

        
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
