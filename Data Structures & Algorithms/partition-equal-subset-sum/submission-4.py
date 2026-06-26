class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        
        if total % 2 != 0:
            return False
        
        memo = {}
        def dfs(i, curSum):
            if curSum == total/2:
                return True
            if i >= len(nums):
                return False
            key = (i, curSum)
            if key in memo:
                return memo[key]
            
            memo[key] = dfs(i+1, curSum+nums[i]) or dfs(i+1, curSum)
            return memo[key]

        return dfs(0,0)

