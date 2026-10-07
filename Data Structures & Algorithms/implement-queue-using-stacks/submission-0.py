class MyQueue:

    def __init__(self):
        self.queue = deque([])
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        print(self.queue)
        

    def pop(self) -> int:
        return self.queue.popleft()
        

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        if len(self.queue) > 0:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()