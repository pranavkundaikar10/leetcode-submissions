class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        maxWater = 0
        while i < j:
            amt = (j - i) * min(heights[i], heights[j])
            print(amt, maxWater)
            maxWater = max(amt, maxWater)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxWater

        