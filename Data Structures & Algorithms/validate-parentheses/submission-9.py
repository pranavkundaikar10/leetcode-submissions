class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bMap = {'}':'{' , ']': '[', ')': '('}
        for i in s:
            print(stack)
            if i not in bMap:
                stack.append(i)
                continue
            if not stack:
                return False
            if stack[-1] != bMap[i]:
                return False
            stack.pop()
        if stack:
            return False
        return True
        