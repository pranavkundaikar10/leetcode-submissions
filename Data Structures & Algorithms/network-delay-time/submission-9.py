class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n+1)}

        for u, v, t in times:
            adj[u].append((t, v))
        
        heap = [(0, k)]
        times = {}

        while heap:
            dst, node = heapq.heappop(heap)
            if node in times:
                continue
            times[node] = dst
            for d, neighbor in adj[node]:
                heapq.heappush(heap, (d+dst, neighbor))
        maxT = 0
        for i in range(1, n+1):
            if i not in times:
                return -1
            maxT = max(maxT, times[i])
        return maxT
            


        