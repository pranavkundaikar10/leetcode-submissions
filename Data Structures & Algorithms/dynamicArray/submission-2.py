class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.len = 0


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.len == self.capacity:
            self.resize()
        self.arr[self.len] = n
        self.len += 1

    def popback(self) -> int:
        val = self.arr[self.len-1]
        self.len -= 1
        return val
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity
        for i in range(self.len):
            newArr[i] = self.arr[i]
        self.arr = newArr


    def getSize(self) -> int:
        return self.len
    
    def getCapacity(self) -> int:
        return self.capacity