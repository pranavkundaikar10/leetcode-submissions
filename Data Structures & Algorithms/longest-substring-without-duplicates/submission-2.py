class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        window = set()
        long_sub = 0
        for j in range(len(s)):
            while s[j] in window:
                window.remove(s[i])
                i += 1
            window.add(s[j])
            long_sub = max(long_sub, len(window))
        return long_sub

        
        