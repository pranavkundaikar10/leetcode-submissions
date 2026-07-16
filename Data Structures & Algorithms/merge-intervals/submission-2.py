class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item:item[0])
        res = [intervals[0]]
        
        for j in range(1, len(intervals)):
            if res[-1][1] < intervals[j][0]:
                res.append(intervals[j])
            else:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[j][1])]
        
        return res
