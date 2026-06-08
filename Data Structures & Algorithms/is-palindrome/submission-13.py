class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            print(s[l], s[r])
            if not self.isAlphaNum(s[l].lower()):
                print("l not alphanum")
                l += 1
                continue
            if not self.isAlphaNum(s[r].lower()):
                print("r not alphanum")
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def isAlphaNum(self, v):
        return (ord('a') <= ord(v) and ord(v) <= ord('z')) or ((ord('0') <= ord(v) <= ord('9')))

        