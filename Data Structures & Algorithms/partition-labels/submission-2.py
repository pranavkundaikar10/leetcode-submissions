class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxIdx = {}

        for i, val in enumerate(s):
            maxIdx[val] = i

        l, r, res = 0, 0, []
        maxEnd = 0
        while r < len(s):
            maxEnd = max(maxEnd, maxIdx[s[r]])
            if r == maxEnd:
                res.append(r-l+1)
                l, r = maxEnd+1, maxEnd+1
            else:
                r += 1

            
        return res
