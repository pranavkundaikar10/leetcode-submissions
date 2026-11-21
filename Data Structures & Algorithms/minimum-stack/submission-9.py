class MinStack:

    def __init__(self):
        self.stack = []


    def push(self, val: int) -> None:
        currMin = self.stack[-1][1] if self.stack else float("inf")
        self.stack.append((val, min(val, currMin)))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1][1]
