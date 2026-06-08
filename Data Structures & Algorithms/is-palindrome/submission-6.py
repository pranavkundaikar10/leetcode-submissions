class Solution:
    def isAlphaNum(self, c: str) -> bool:
        if ord('A') <= ord(c) <= ord('Z') or \
        ord('a') <= ord(c) <= ord('z') or \
        ord('0') <= ord(c) <= ord('9'):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        s = s.lower()
        while i < j:
            print(i, j, s[i], s[j])
            while i < j and not self.isAlphaNum(s[i]):
                print("inside i not alphanum")
                i += 1
            while j > i and not self.isAlphaNum(s[j]):
                print("inside j not alphanum")
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        