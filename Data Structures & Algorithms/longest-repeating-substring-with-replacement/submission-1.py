class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j, res = 0, 0, 0
        count, freq = {}, 0

        while j < len(s):
            count[s[j]] = count.get(s[j], 0) + 1
            freq = max(freq, count[s[j]])
            while (j - i + 1) - freq > k:
                count[s[i]] = count.get(s[i], 0) - 1
                i += 1
            res = max(res, j-i+1)
            j += 1

        return res