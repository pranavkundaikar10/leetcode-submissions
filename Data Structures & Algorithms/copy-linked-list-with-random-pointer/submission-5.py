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
        mp = {}
        if not head:
            return

        def dfs(root):
            if not root:
                return
            node = Node(root.val)
            mp[root] = node
            if root.next and root.next not in mp:
                dfs(root.next)
            node.next = mp[root.next] if root.next else None
            if root.random and root.random not in mp:
                dfs(root.random)
            node.random = mp[root.random] if root.random else None

        dfs(head)
        return mp[head]
