class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, height in enumerate(heights):
            currIdx = i
            while stack and stack[-1][1] > height:
                j, h = stack.pop()
                currIdx = j
                res = max(res, (h * (i - j)))
            stack.append((currIdx, height))
        
        for i, height in stack:
            res = max(res, (height*(len(heights)-i)))
        return res
