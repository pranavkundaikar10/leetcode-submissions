class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b):
            return a+b
        def subtract(a, b):
            return a - b
        def multiply(a, b):
            return a * b
        def divide(a, b):
            return int(float(a)/b)
        stack = []
        operands = {'+':add, '-':subtract, '*':multiply, '/':divide}
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
                continue
            if len(stack) < 2:
                print("stack len less than 2", token)
                print(stack)
                return False
            b, a = int(stack.pop()), int(stack.pop())
            print(a, b)
            stack.append(operands.get(token)(a,b))
        if len(stack) > 1:
            print("stack len more than 1")
            return False
        return stack[0]
    

        