"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nmap = {}

        def dfs(root):
            if not root:
                return

            new_node = Node(root.val)
            nmap[root] = new_node

            for neighbor in root.neighbors:
                if neighbor not in nmap:
                    dfs(neighbor)
                new_node.neighbors.append(nmap[neighbor])
        dfs(node)
        return nmap.get(node, None)
