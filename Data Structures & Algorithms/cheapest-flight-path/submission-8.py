class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0
        print(dist)

        for i in range(k+1):
            new_dist = dist.copy()

            for u, v, c in flights:
                new_dist[v] = min(new_dist[v], dist[u]+c)

            dist = new_dist.copy()
        
        return dist[dst] if dist[dst] != float("inf") else -1


