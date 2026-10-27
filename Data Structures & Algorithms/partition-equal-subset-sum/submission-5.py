class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        memo = {}

        def dfs(i, remaining):
            if remaining == 0:
                return True
            if i >= len(nums) or remaining < 0:
                return False
            key = (i, remaining)
            if key in memo:
                return memo[key]
            
            memo[key] = dfs(i+1, remaining) or dfs(i+1, remaining-nums[i])
            return memo[key]
        return dfs(0, sum(nums)//2)
            

        