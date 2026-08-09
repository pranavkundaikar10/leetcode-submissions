class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        print(len(adj))

        for u, v, t in times:
            adj[u].append((v, t))
        
        heap = [(0, k)]
        visited = [-1] * (n+1)

        while heap:
            t, node = heapq.heappop(heap)
            print(f'node: {node} {t} {visited}')
            if visited[node] != -1:
                continue
            visited[node] = t
            for neighbor, time in adj[node]:
                if visited[neighbor] != -1:
                    continue
                heapq.heappush(heap, (t+time, neighbor))

        maxT = 0
        print(visited, adj)
        print(f'heap {heap}')
        for i in range(1, len(visited)):
            if visited[i] == -1:
                return -1
            maxT = max(maxT, visited[i])

        return maxT

