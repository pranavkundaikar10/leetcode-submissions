class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 0
        l, r = 0, 0
        window = {}
        max_count = 0
        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            max_count = max(max_count, window[s[r]])
            while (r-l+1) - max_count > k:
                window[s[l]] -= 1
                l += 1
            output = max(output, r-l+1)
            r +=1
        return output
        