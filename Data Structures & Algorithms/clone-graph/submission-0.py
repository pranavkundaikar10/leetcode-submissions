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
        clones = collections.defaultdict(lambda:Node(0))
        queue = collections.deque([node])
        seen = set([node])
        while queue:
            for i in range(len(queue)):
                v = queue.popleft()
                clone_v = clones[v]
                clone_v.val = v.val
                for neighbor in v.neighbors:
                    clone_v.neighbors.append(clones[neighbor])
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)
        return clones[node]