class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if target == total else 0
            
            key = (i, total)
            if key in memo:
                return memo[key]
            
            memo[key] = backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i])
            return memo[key]


        return backtrack(0, 0)