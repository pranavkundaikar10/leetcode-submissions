"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pointer_map = {}
        curr = head
        while curr:
            pointer_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        new_head = pointer_map[curr] if curr else None
        while curr:
            pointer_map[curr].val = curr.val
            pointer_map[curr].next = pointer_map[curr.next] if curr.next else None
            pointer_map[curr].random = pointer_map[curr.random] if curr.random else None
            curr = curr.next
        return new_head


        