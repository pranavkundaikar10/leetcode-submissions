class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i, val in enumerate(s):
            lastIdx[val] = i

        
        start, end = 0, 0
        res = []
        for i in range(len(s)):
            end = max(end, lastIdx[s[i]])
            if i == end:
                res.append(end-start+1)
                end, start = end +1, end+1
        return res

