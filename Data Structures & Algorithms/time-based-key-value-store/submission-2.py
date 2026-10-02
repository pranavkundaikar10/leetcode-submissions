class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.cache[key]
        l, r = 0, len(arr)
        res = ""
        # finding upper bound one greater than our index
        # loop ends when l == r giving us the boundary
        while l < r:
            m = l + (r - l) // 2
            if arr[m][0] > timestamp:
                r = m
            else:
                l = m + 1
        # checking if the previous value is valid before returning
        # l contains the upper boundary
        if l > 0 and arr[l-1][0] <= timestamp:
            return arr[l-1][1]
        return ""


        
