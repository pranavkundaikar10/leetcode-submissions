"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        end = sorted([i.end for i in intervals])
        start = sorted([i.start for i in intervals])

        count = 0
        res = 0
        i, j = 0, 0
        while j < len(intervals):
            if i < len(intervals) and start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(count, res)
        return res

