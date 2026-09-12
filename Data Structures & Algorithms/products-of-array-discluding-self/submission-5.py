class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preF = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= preF
            preF *= nums[i]

        preF = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= preF
            preF *= nums[i]

        return res
