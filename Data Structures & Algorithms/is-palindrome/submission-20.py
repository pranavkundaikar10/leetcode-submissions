class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l <= r:
            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            if not self.isAlphaNum(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -= 1
        return True

    def isAlphaNum(self, c):
        if not ((ord('0') <= ord(c) <= ord('9')) or (ord('a') <= ord(c.lower()) <= ord('z'))):
            return False
        return True
