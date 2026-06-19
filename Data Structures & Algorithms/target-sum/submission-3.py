class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def dfs(i, total):
            nonlocal res
            if i == len(nums):
                if total == target:
                    res += 1
                return
            dfs(i+1, total + nums[i])
            dfs(i+1, total - nums[i])

        dfs(0, 0)
        return res