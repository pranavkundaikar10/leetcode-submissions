class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for x, y in points:
            d = -math.sqrt(y**2 + x**2)
            distance.append((d, [x,y]))
        heapq.heapify(distance)
        while len(distance) > k:
            heapq.heappop(distance)
        return [y for x, y in distance]    