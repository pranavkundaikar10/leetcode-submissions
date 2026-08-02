class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]

        for src, dst, time in times:
            adj[src].append((time, dst))
        
        target = {}
        for i in range(1, n+1):
            target[i] = -1
        heap = [(0, k)]
        while heap:
            dst, node = heapq.heappop(heap)
            if target[node] != -1:
                continue
            
            target[node] = dst
            for d, neighbor in adj[node]:
                if target[neighbor] != -1:
                    continue
                heapq.heappush(heap, (d+dst, neighbor))

        for i in target:
            if target[i] == -1:
                return -1
        
        return max(target.values())