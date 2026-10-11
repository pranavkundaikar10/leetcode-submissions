class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.large, num)

        if self.small and self.large and self.large[0] > self.small[0]:
            val = heapq.heappop_max(self.large)
            heapq.heappush(self.small, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop_max(self.large)
            heapq.heappush(self.small, val)

        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush_max(self.large, val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]

        if len(self.large) >len(self.small):
            return self.large[0]

        return (self.small[0] + self.large[0])/2
        
        