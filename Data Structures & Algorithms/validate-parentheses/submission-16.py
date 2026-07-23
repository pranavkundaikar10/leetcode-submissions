class Solution:
    def isValid(self, s: str) -> bool:
        mp = {']':'[', '}':'{', ')': '('}
        stack = []
        for val in s:
            if val in mp:
                if not stack or stack[-1] != mp[val]:
                    return False
                stack.pop()
                continue
            stack.append(val)
        return True if not stack else False