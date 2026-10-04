class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = float("inf") if not self.stack else self.stack[-1][1]
        self.stack.append((val, min(curr_min, val)))

    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0] if self.stack else -1

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else -1
        
