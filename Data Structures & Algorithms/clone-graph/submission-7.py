"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        mp = {node:Node(node.val)}
        queue = deque([node])
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in mp:
                    mp[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)                    
                mp[n].neighbors.append(mp[neighbor])

        return mp[node]
                

