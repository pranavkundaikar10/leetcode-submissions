class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {']':'[', '}': '{', ')': '('}
        stack = []
        for c in s:
            if c not in bmap:
                stack.append(c)
            else:
                if not stack or stack[-1] != bmap[c]:
                    return False
                stack.pop()
        
        return True if not stack else False