class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]

        for u, v, t in times:
            adj[u].append((t, v))
        
        queue = [(0, k)]
        times = {i:-1 for i in range(1, n+1)}
        while queue:
            dst, node = heapq.heappop(queue)
            if times[node] != -1:
                continue
            times[node] = dst
            for d, n in adj[node]:
                if times[n] != -1:
                    continue
                heapq.heappush(queue, (dst+d, n))
        maxT = 0
        for key, val in times.items():
            if val == -1:
                return -1
            maxT = max(val, maxT)

        return maxT
