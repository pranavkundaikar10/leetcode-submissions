class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def backtrack(i, total):
            if i >= len(nums):
                return total
            key = (i, total)
            if key in memo:
                return memo[key]

            memo[key] = max(backtrack(i+1, total), backtrack(i+2, total + nums[i]))
            return memo[key]
        return backtrack(0, 0)
            
