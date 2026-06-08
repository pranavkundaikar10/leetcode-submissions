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
        ll = collections.defaultdict(lambda:Node(0, None))
        ll[None] = None
        curr = head
        while curr:
            ll[curr].val = curr.val
            ll[curr].next = ll[curr.next] if curr.next else None
            ll[curr].random = ll[curr.random] if curr.random else None
            curr = curr.next
        return ll.get(head)
        