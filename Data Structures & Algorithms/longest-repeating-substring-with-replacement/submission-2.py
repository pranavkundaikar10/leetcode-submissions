class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, res = 0, 0, 0
        freq = defaultdict(int)
        maxF = 0
        while r < len(s):
            freq[s[r]] += 1
            maxF = max(maxF, freq[s[r]])
            while (r-l+1) - maxF > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
            r+=1
        return res

