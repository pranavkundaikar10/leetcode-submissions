class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def dfs(i, sum):
            nonlocal res
            if i > len(nums)-1:
                if sum == target:
                    res += 1
                return
            dfs(i+1, sum + nums[i])
            dfs(i+1, sum - nums[i])

        dfs(0, 0)
        return res


        