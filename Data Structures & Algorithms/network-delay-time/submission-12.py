class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {i:[] for i in range(1, n+1)}

        for u, v, t in times:
            adj[u].append((v, t))
        
        heap = [(0, k)]
        times = {}

        while heap:
            time, node = heapq.heappop(heap)
            if node in times:
                continue
            times[node] = time

            for neighbor, t in adj[node]:
                if neighbor in times:
                    continue
                heapq.heappush(heap, (time+t, neighbor))
        maxT = 0
        for node in adj:
            if node not in times:
                return -1
            maxT = max(maxT, times[node])
        
        return maxT



