class Solution:
    def rob(self, nums: List[int]) -> int:
        opt = {-1:0, -2: 0}
        for i in range(len(nums)):
            if i < 0:
                return
            opt[i] = max(opt[i-1], nums[i] + opt[i-2])
        return opt[len(nums)-1]
        