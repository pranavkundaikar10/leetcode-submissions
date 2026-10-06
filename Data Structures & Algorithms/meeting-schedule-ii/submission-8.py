"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        end = [i.end for i in intervals]
        start = [i.start for i in intervals]
        start.sort()
        end.sort()

        count, res = 0, 0

        i, j = 0, 0

        while j < len(end):
            if i < len(start) and start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res




        