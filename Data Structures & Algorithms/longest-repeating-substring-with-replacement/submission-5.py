class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL, res = 0, 0
        l, r = 0, 0 
        counts = defaultdict(int)
        while r < len(s):
            counts[s[r]] += 1
            maxL = max(maxL, counts[s[r]])
            if (r-l+1) - maxL > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res

