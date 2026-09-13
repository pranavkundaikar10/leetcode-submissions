class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax, currMax, currMin = nums[0], nums[0], nums[0]
        if not nums:
            return 0

        for num in nums[1:]:
            if num < 0:
                currMax, currMin = currMin, currMax
            currMax = max(num, currMax * num)
            currMin = min(num, currMin * num)
            globalMax = max(globalMax, currMax)
        return globalMax