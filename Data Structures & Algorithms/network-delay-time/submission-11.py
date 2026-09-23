class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]

        for u, v, t in times:
            adj[u].append((v, t))

        res = {}
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if node in res:
                continue
            res[node] = time
            for neighbor, t in adj[node]:
                if neighbor in res:
                    continue
                heapq.heappush(heap,(t+time, neighbor))
        maxT = -1
        for i in range(1, n+1):
            if i not in res:
                return -1
            maxT = max(maxT, res[i])
        return maxT


            



            

        