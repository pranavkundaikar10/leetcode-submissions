class FreqStack:

    def __init__(self):
        self.cnts = {}
        self.maxCnt = 0
        self.stacks = {}
        

    def push(self, val: int) -> None:
        valCnt = 1 + self.cnts.get(val, 0)
        self.cnts[val] = valCnt
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stacks[self.maxCnt] = []
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnts[res] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()