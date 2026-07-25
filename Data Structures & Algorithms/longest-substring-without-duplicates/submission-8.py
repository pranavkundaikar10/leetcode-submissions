class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l, r, res = 0, 0, 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            seen.add(s[r])
            r += 1
        return res
