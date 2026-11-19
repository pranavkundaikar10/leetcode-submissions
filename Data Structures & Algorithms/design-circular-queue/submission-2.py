class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.count = 0
        

    def enQueue(self, value: int) -> bool:
        # print(self.queue, self.front, self.rear)
        if self.isFull():
            return False

        self.count += 1
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value        
        return True
        

    def deQueue(self) -> bool:
        # print(self.queue, self.front, self.rear)
        if self.isEmpty():
            return False
        self.queue[self.front] = None
        self.count -= 1
        self.front = (self.front + 1) % self.capacity
        return True


    def Front(self) -> int:
        # print(self.queue, self.front, self.rear)      
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        # print(self.queue, self.front, self.rear)
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count >= self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()