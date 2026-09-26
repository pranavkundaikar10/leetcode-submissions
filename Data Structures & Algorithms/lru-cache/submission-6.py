class ListNode:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache.get(key)
        self._remove(node)
        self._add_to_head(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
        self._add_to_head(node)
        if len(self.cache) > self.capacity:
            self.cache.pop(self.tail.prev.key)
            self._remove(self.tail.prev)


    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev, self.head.next = node, node
        
