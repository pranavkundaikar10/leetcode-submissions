class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        nums.sort()
        def dfs(i, sum):
            if sum == target:
                res.append(subset.copy())
                return
            if i == len(nums) or sum > target:
                return
            subset.append(nums[i])
            dfs(i, sum + nums[i])
            # dfs(i+1, sum + nums[i])
            subset.pop()
            # while i + 1 < len(nums) and nums[i] == nums[i+1]:
            #     i += 1
            dfs(i+1, sum)
        dfs(0, 0)
        return res
        