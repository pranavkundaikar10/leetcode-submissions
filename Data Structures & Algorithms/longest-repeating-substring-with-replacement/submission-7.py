class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(int)
        l, r = 0, 0
        maxF, res = 0, 0
        while r < len(s):
            freqMap[s[r]] += 1
            maxF = max(maxF, freqMap[s[r]])
            if r - l + 1 - maxF > k:
                freqMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res