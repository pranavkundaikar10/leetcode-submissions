class Solution:
    def isValid(self, s: str) -> bool:
        output = True
        mapp = {')': '(', ']':'[', '}':'{'}
        stack = []
        for val in s:
            if val in mapp:
                if not stack:
                    output = False
                    break
                item = stack.pop()
                if item != mapp.get(val):
                    output = False
                    break
            else:
                stack.append(val)
        if stack:
            output = False
        
        return output