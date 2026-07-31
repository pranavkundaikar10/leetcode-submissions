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
        nodes = defaultdict(Node)

        def dfs(root):
            # nonlocal nodes
            if root in nodes:
                return
            new_node = nodes[root.val]
            new_node.val = root.val
            for n in root.neighbors:
                # n_node = nodes[n.val]
                if n.val not in nodes:
                    dfs(n)
                new_node.neighbors.append(nodes[n.val])
        dfs(node)
        return nodes[node.val]



