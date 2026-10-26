class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float("inf")] * n
        dist[src] = 0

        for i in range(k+1):
            new_dist = dist.copy()

            for u, v, w in flights:
                new_dist[v] = min(new_dist[v], dist[u]+w)
            dist = new_dist

        return dist[dst] if dist[dst] != float("inf") else -1
