class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_map = {']': '[', '}':'{', ')': '('}
        for c in s:
            if c in b_map:
                if not stack or stack[-1] != b_map.get(c):
                    return False
                stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        return True

        