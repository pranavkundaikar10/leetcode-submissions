class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        distance = [float("inf")] * n
        distance[src] = 0

        for _ in range(k+1):
            new_dst = distance.copy()

            for u, v, c in flights:
                if new_dst[u] != float("inf") and distance[u] + c < new_dst[v]:
                    new_dst[v] = distance[u] + c

            distance = new_dst

        return distance[dst] if distance[dst] != float("inf") else -1


