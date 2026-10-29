class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        leftMax, rightMax = 0, 0
        res = 0
        while l <= r:
            if leftMax <= rightMax:
                res += max(min(leftMax,rightMax) - height[l], 0)
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                res += max(min(leftMax,rightMax) - height[r], 0)
                rightMax = max(rightMax, height[r])                
                r -= 1

        return res

