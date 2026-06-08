class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            if not self.isAlphaNum(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def isAlphaNum(self, s):
        return (ord('a') <= ord(s) <= ord('z') or ord('0') <= ord(s) <= ord('9') or ord('A') <= ord(s) <= ord('Z'))

        