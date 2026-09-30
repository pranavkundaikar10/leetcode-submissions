class Logger:

    def __init__(self):
        self._cache = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._cache:
            self._cache[message] = timestamp
            return True
        
        if timestamp - self._cache[message] < 10:
            return False
        self._cache[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
