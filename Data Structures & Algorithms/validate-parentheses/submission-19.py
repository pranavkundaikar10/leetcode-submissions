class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {'}': '{', ')': '(', ']':'['}
        for val in s:
            if val not in mp:
                stack.append(val)
                continue
            if not stack or stack[-1] != mp[val]:
                return False
            stack.pop()
        
        return True if not stack else False

            



