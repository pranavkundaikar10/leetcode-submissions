class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def backtrack(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(backtrack(i+1), (backtrack(i+2)+nums[i]))
            return memo[i]

        return backtrack(0)