class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        max_len = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            max_len = max(max_len, r - l + 1)
            seen.add(s[r])
            r += 1
        return max_len
        