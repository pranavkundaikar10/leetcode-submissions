class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            new_idx = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                width = i - idx
                area = width * height
                res = max(res, area)
                new_idx = idx
            stack.append((new_idx, h))
        
        while stack:
            idx, height = stack.pop()
            width = len(heights) - idx
            area = width * height
            res = max(res, area)

        return res