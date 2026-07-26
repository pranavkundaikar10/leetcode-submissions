class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        prevMin = float("inf")
        if self.stack:
            prevMin = self.stack[-1][1]
        self.stack.append((val, min(prevMin, val)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
