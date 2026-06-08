class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
    
    def print(self):
        print("inside print")
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        if not self.head:
            self.tail = node
        self.head = node
        self.print()
        

    def insertTail(self, val: int) -> None:
        if not self.tail:
            return self.insertHead(val)
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.print()

    def remove(self, index: int) -> bool:
        if index == 0:
            if not self.head:
                return False
            self.head = self.head.next
            return True
        # 5, 2, 1, 3, 4
        # 0, 1, 2, 3, 4
        prev = self.head
        curr = self.head.next
        i = 1
        while curr:
            if i == index:
                if curr == self.tail:
                    self.tail = prev
                prev.next = curr.next
                return True
            curr = curr.next
            prev = prev.next
            i += 1
        return False
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
