class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1F, s2F = [0] * 26, [0] * 26
        for s in s1:
            s1F[ord(s)-ord('a')] += 1
        l, r = 0, 0

        while r < len(s2):
            s2F[ord(s2[r])-ord('a')] += 1
            while r - l + 1 > len(s1):
                s2F[ord(s2[l])-ord('a')] -= 1
                l += 1
            if s2F == s1F:
                return True
            r += 1
        return False


        


