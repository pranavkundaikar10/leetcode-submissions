class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            maxP = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxP = max(maxP, dp[j])
            dp[i] = 1 + maxP

        return max(dp)
