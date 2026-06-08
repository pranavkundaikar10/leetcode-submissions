class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i, curr = 0, self.head
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head = node


    def insertTail(self, val: int) -> None:
        node = Node(val)
        if not self.tail:
            self.head = self.tail = node
            return
        self.tail.next = node
        self.tail = node
        

    def remove(self, index: int) -> bool:
        i, curr, prev = 0, self.head, Node(0, self.head)
        while curr:
            if i != index:
                prev = curr
                curr = curr.next
                i += 1
                continue
            prev.next = curr.next
            if curr == self.head:
                self.head = prev.next
            if curr == self.tail:
                self.tail = prev
            return True
        return False
        

    def getValues(self) -> List[int]:
        res, curr = [], self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
        
