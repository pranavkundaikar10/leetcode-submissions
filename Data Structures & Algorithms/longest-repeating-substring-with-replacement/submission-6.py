class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxF = 0, 0, 0
        mp = defaultdict(int)
        res = 0
        while r < len(s):
            mp[s[r]] += 1
            maxF = max(maxF, mp[s[r]])
            if (r - l + 1) - maxF > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
