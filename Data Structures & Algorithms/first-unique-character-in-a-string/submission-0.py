class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = [-1] * 26
        for i in range(len(s)):
            seen[ord(s[i])-ord('a')] += 1
        
        for i in range(len(s)):
            if seen[ord(s[i])-ord('a')] == 0:
                return i
        return -1




