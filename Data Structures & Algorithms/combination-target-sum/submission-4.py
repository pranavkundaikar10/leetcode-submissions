class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, subset, sum):
            if sum > target:
                return
            if sum == target:
                res.append(subset[:])
                return

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j, subset, sum+nums[j])
                subset.pop()

        dfs(0, [], 0)
        return res