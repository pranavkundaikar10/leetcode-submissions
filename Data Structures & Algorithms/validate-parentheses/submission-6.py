class Solution:
    def isValid(self, s: str) -> bool:
        map = {']': '[', '}':'{', ')':'('}
        stack = []
        for i in s:
            if i not in map:
                stack.append(i)
                continue
            if not stack:
                return False
            if map[i] != stack.pop():
                return False
        
        if stack:
            return False
        return True
                
        