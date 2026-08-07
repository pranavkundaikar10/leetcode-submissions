class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i

        start, end = 0, 0
        res = []
        for i in range(len(s)):
            end = max(end, lastIndex[s[i]])
            if i == end:
                res.append(end-start+1)
                start, end = i + 1, i+1
        return res

