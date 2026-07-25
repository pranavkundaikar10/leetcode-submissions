class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1] * len(nums)
        for i, num in enumerate(nums):
            res[i] *= prefix
            prefix *= num
        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prefix
            prefix *= nums[i]
        return res
