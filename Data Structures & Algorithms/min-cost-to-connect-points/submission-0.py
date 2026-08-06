class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = [False] * len(points)
        connected = 0
        heap = [(0, 0)]
        total_cost = 0
        while heap:
            cost, pt = heapq.heappop(heap)
            if visited[pt]:
                continue
            visited[pt] = True
            connected += 1
            total_cost += cost
            if connected == len(points):
                return total_cost
            for i in range(len(points)):
                if not visited[i]:
                    dist = abs(points[pt][0]-points[i][0])+ abs(points[pt][1]-points[i][1])
                    heapq.heappush(heap,(dist, i))

                
        return -1

