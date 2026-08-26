class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        for u, v, t in times:
            adj[u].append((t, v))

        heap = [(0, k)]

        time = {}
        while heap:
            dst, node = heapq.heappop(heap)
            if node in time:
                continue
            time[node] = dst
            for t, nei in adj[node]:
                if nei in time:
                    continue
                heapq.heappush(heap, (dst+t, nei))
        maxT = 0
        for i in range(1, n+1):
            if i not in time:
                return -1
            maxT = max(maxT, time[i])
        
        return maxT
        