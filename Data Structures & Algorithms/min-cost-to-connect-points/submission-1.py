class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges, res = 0, 0
        node, n = 0, len(points)
        visited = [False] * n
        dist = [float("inf")] * n
        while edges < n-1:
            visited[node] = True
            nextNode = -1
            edges += 1            
            for i in range(n):
                if visited[i]:
                    continue
                currDist = abs(points[node][0]-points[i][0]) + abs(points[node][1]-points[i][1])
                dist[i] = min(dist[i], currDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            node = nextNode
            res += dist[node]

        return res