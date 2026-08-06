class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for i in range(n)]
        for s, d, p in flights:
            adj[s].append((d, p))
        
        min_stops = [float('inf')] * n
        heap = [(0, 0, src)]

        while heap:
            price, stops, destination = heapq.heappop(heap)
            if stops > k+1 or stops >= min_stops[destination]:
                continue
            
            if destination == dst:
                return price
            
            min_stops[destination] = stops

            for neighbor, cost in adj[destination]:
                heapq.heappush(heap, (price+cost, stops+1, neighbor))

        return -1
