class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford
        distance = {i: float("inf") for i in range(n)}
        distance[src] = 0

        for i in range(k+1):
            new_dst = distance.copy()

            for s, d, c in flights:
                new_dst[d] = min(new_dst[d], distance[s]+c)
            
            distance = new_dst.copy()
        
        return distance[dst] if distance[dst] != float("inf") else -1





        


