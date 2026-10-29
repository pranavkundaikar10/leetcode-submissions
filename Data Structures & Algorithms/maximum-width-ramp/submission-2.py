class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        proc = [0] * len(nums)
        proc[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            if proc[i+1] >= nums[i]:
                proc[i] = proc[i+1]
            else:
                proc[i] = nums[i]
        
        res = 0
        l, r = 0, 1

        while r < len(nums):
            while nums[l] > proc[r]:
                l += 1
            res = max(res, r - l)
            r += 1
        return res




 
