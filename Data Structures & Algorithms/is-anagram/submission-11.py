class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cs = [0]*26
        for i in range(len(s)):
            cs[ord(s[i])-ord('a')] += 1
            cs[ord(t[i])-ord('a')] -= 1
        
        for i in cs:
            if i != 0:
                return False
        return True
        