class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap = []
        for num in arr:
            heapq.heappush(heap, (abs(num-x), num))
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k-= 1
        res.sort()
        return res
        