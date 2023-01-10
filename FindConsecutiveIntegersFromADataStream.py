class DataStream:

    streamCounter = 0
    value = 0
    k = 0

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.streamCounter += 1
            if self.k <= self.streamCounter:
                return True
            else:
                return False
        else:
            self.streamCounter = 0
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
