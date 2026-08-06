class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for i in range(n)]
        for s, d, p in flights:
            adj[s].append((p, d))
        
        heap = [(0, 0, src)]
        min_stops = [float('inf')]*n

        while heap:
            price, stops, node = heapq.heappop(heap)



            if stops >= min_stops[node] or stops > k+1:
                continue
            if node == dst:
                return price
            min_stops[node] = stops

            for cost, neighbor in adj[node]:
                heapq.heappush(heap, (price+cost, stops+1, neighbor))
        return -1