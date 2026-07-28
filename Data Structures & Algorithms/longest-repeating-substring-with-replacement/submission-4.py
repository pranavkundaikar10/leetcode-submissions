class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, res, maxF = 0, 0, 0, 0
        mp = defaultdict(int)
        while r < len(s):
            mp[s[r]] += 1
            maxF = max(maxF, mp[s[r]])
            while r-l+1 - maxF > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
