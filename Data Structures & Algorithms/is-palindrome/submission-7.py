class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not self.isAlpha(s[l].lower()):
                l += 1
                continue
            if not self.isAlpha(s[r].lower()):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    def isAlpha(self, s):
        return (ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z') or ord('0') <= ord(s) <= ord('9'))
        


        