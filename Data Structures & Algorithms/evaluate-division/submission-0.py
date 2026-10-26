class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            u, v = equations[i]
            adj[u].append((values[i], v))
            adj[v].append((1/values[i], u))

        res = []
        for src, dst in queries:
            val = -1
            if src not in adj:
                res.append(val)
                continue
            queue = deque([(1, src)])
            visited = {src}
            while queue:
                value, node = queue.popleft()
                if node == dst:
                    val = value
                    break
                for v, neigh in adj[node]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    queue.append((value * v, neigh))
            res.append(val)
        return res
            



            


