class LogSystem:

    def __init__(self):
        self.logs = []
        self.gran = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }


    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))
        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        gran = self.gran[granularity]
        s, e = start[:gran], end[:gran]
        res = [log[0]for log in self.logs if s <= log[1][:gran] <= e]
        return res
            


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
