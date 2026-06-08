class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        sum = 0
        def dfs(i, sum):
            if sum == target:
                res.append(subset.copy())
                return
            if i > len(nums)-1 or sum > target:
                return
            sum += nums[i]
            subset.append(nums[i])
            dfs(i, sum)
            subset.pop()
            sum -= nums[i]
            dfs(i+1, sum)
        dfs(0, 0)
        return res

        