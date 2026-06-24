class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total = 0
        for num in nums:
            total += num

        if total % 2 != 0:
            return False

        def dfs(i, currSum):

            if currSum == total / 2:
                return True

            if currSum > total / 2 or i >= len(nums):
                return False

            key = (i, currSum)
            if key in memo:
                return memo[key]

            memo[key] = dfs(i+1, currSum + nums[i]) or dfs(i+1, currSum)
            return memo[key]

        return True if dfs(0, 0) else False