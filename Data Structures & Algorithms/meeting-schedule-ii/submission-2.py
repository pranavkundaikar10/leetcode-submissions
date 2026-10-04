"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = [i.start for i in intervals]
        end_times = [i.end for i in intervals]
        start_times.sort()
        end_times.sort()

        s, e, count, res = 0, 0, 0, 0
        while s < len(intervals):
            if start_times[s] < end_times[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
            