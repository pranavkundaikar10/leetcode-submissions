class StringIterator:

    def __init__(self, compressedString: str):
        self.string = compressedString
        self.i = 0
        self.count = 0
        self.val = ' '


    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.count > 0:
            self.count -= 1
            return self.val
        self.val = self.string[self.i]
        i = self.i
        j = self.i + 1

        while self.string[j].isdigit():
            j += 1
        count = self.string[self.i+1:j]
        self.count = int(count)
        self.i = j
        self.count -= 1
        return self.val


        

    def hasNext(self) -> bool:
        return self.i < len(self.string) or self.count > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
