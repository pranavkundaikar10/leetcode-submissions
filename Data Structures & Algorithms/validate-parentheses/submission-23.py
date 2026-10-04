class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bmap = {']':'[', ')':'(', '}':'{'}

        for c in s:
            if c not in bmap:
                stack.append(c)
                continue
            if not stack or stack[-1] != bmap[c]:
                return False
            stack.pop()
        return True if not stack else False

