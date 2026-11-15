class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))

        heap = [(0, k)]
        visited = set()

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time
            for t, neighbor in adj[node]:
                if neighbor in visited:
                    continue
                heapq.heappush(heap, (t+time, neighbor))
        return -1
            