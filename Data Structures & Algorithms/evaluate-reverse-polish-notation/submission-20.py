class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mp = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: int(a / b)
        }
        stack = []

        for i in tokens:
            if i not in mp:
                stack.append(int(i))
                continue
            b, a = stack.pop(), stack.pop()
            stack.append(mp[i](a, b))
        return stack[-1]
