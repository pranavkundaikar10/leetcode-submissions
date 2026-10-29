class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(len(nums)):
            if not (increasing or decreasing):
                return False

            if i > 0 and nums[i] < nums[i-1]:
                increasing = False
            
            if i > 0 and nums[i] > nums[i-1]:
                decreasing = False

        return increasing or decreasing
        



        