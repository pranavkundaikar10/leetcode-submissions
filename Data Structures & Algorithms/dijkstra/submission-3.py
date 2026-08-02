class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = [[] for i in range(n)]

        for u, v, d in edges:
            adj[u].append((d, v))
        target = {}
        heap = [[0, src]]
        while heap:
            d, node = heapq.heappop(heap)
            if node in target:
                continue
            target[node] = d
            for dist, neighbor in adj[node]:
                if neighbor not in target:
                    heapq.heappush(heap, [d+dist, neighbor])

        for i in range(n):
            if i not in target:
                target[i] = -1
        return target

