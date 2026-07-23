class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mp = {'+': self.add, '-':self.sub, '*': self.mul, '/':self.div}
        stack = []
        for v in tokens:
            print(stack)
            if v not in mp:
                stack.append(int(v))
                continue
            b, a = stack.pop(), stack.pop()
            val = mp[v](a, b)
            stack.append(val)
        print(stack)
        return stack[-1]
            
    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b
    
    def sub(self, a, b):
        return a - b
    
    def div(self, a, b):
        return int(a / b)