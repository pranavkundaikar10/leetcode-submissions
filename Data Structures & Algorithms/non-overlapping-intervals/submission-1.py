class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item:item[0])
        prevEnd, res = float('-inf'), 0
        for i in intervals:
            if i[0] >= prevEnd:
                prevEnd = i[1]
            else:
                prevEnd = min(i[1], prevEnd)
                res += 1
        return res