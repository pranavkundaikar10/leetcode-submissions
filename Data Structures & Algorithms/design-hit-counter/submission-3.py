class HitCounter:

    def __init__(self):
        self.hits = deque()
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        diff = timestamp - self.hits[0]
        while diff >= 300:
            if not self.hits:
                break
            self.hits.popleft()
            if not self.hits:
                break            
            diff = timestamp - self.hits[0]
        return len(self.hits)

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
