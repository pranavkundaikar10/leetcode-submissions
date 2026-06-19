class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def dfs(i, total, subset):
            nonlocal res
            if i == len(nums):
                if total == target:
                    res += 1
                return
            subset.append(nums[i])
            dfs(i+1, total + nums[i], subset)
            subset.pop()
            subset.append(-nums[i])            
            dfs(i+1, total - nums[i], subset)

        dfs(0, 0, [])
        return res