class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord('a') - ord(s[i].lower())] += 1
            count[ord('a') - ord(t[i].lower())] -= 1
        for val in count:
            if val != 0:
                return False
        return True
        