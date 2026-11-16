class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mp = {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y,
            "/" : lambda x, y: x / y
        }

        stack = []
        for ch in tokens:
            if ch == "+":
                y, x = stack.pop(), stack.pop()
                stack.append(x + y)
            elif ch == "-":
                y, x = stack.pop(), stack.pop()                
                stack.append(x - y)
            elif ch == "*":
                y, x = stack.pop(), stack.pop()
                stack.append(x * y)
            elif ch == "/":
                y, x = stack.pop(), stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(ch))
        return stack[-1]

        