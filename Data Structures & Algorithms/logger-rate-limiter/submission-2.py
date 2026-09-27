class Logger:

    def __init__(self):
        self.cache = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.cache:
            self.cache[message] = timestamp
            return True

        if timestamp - self.cache[message] >= 10:
            self.cache[message] = timestamp
            return True
        
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
