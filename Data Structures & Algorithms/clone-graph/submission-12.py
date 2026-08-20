"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}

        def dfs(root):
            if not root:
                return
            mp[root] = Node(root.val)

            for n in root.neighbors:
                if n not in mp:
                    dfs(n)
                mp[root].neighbors.append(mp[n])
        dfs(node)
        return mp[node] if node in mp else None