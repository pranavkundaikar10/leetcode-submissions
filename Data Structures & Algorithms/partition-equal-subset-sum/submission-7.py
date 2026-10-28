class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if (target) % 2 != 0:
            return False

        rows, cols = len(nums) + 1, target//2 + 1

        dp = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            dp[i][0] = True

        for i in range(len(nums)-1, -1, -1):
            for j in range(target//2+1):
                skip = dp[i+1][j]
                take = False
                if nums[i] <= j:
                    take = dp[i+1][j - nums[i]]
                dp[i][j] = skip or take
        return dp[0][target//2]



        