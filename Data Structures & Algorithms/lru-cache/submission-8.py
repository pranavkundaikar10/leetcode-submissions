class ListNode:

    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        node = self.keys[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            self._remove(node)
        else:
            node = ListNode(key=key, val=value)
            self.keys[key] = node
        node.val = value
        self._add_to_head(node)
        if len(self.keys) > self.capacity:
            self.keys.pop(self.tail.prev.key)
            self._remove(self.tail.prev)

    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


        
