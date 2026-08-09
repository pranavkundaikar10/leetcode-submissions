class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]

        for u, v, t in times:
            adj[u].append((t, v))
        
        heap = [(0, k)]
        visited = {i:-1 for i in range(1, n+1)}
        while heap:
            time, node = heapq.heappop(heap)
            if visited[node] != -1:
                continue
            visited[node] = time
            for t, neighbor in adj[node]:
                if visited[neighbor] != -1:
                    continue
                heapq.heappush(heap, (t+time, neighbor))
        maxT = -1
        for i in range(1, n+1):
            if visited[i] == -1:
                return -1
            maxT = max(maxT, visited[i])
        return maxT
            


