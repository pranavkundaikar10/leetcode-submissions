class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        nums = candidates
        res = []
        subset = []
        def dfs(i, sum):
            if sum == target:
                res.append(subset.copy())
                return
            if i > len(nums)-1 or sum > target:
                return
            subset.append(nums[i])
            dfs(i+1, sum + nums[i])
            subset.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i +=1
            dfs(i+1, sum)
        dfs(0, 0)
        return res
        