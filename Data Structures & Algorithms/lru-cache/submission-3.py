class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        print(f'node{node}')
        if node:
            node.val = value
            self._remove(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
        self._add_to_head(node)
        if len(self.cache) > self.cap:
            self.cache.pop(self.tail.prev.key)
            self._remove(self.tail.prev)

    def _add_to_head(self, node):
        node.prev, node.next = self.head, self.head.next        
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        
