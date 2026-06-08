class Node:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if not self.head:
            return True
        return False
        

    def append(self, value: int) -> None:
        node = Node(value)
        if not self.tail:
            self.head = self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        

    def appendleft(self, value: int) -> None:
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        self.head.prev = node
        node.next = self.head
        self.head = node


    def pop(self) -> int:
        if not self.tail:
            return -1
        val = self.tail.val            
        if self.tail == self.head:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return val
        

    def popleft(self) -> int:
        if not self.head:
            return -1
        val = self.head.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        return val
        
