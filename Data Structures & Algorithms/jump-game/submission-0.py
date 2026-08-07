class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i+nums[i])
            if farthest >= len(nums):
                return True
        return True