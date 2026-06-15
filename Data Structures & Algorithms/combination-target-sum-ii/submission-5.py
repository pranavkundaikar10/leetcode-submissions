class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = candidates
        nums.sort()
        def dfs(i, subset, sum):
            if sum == target:
                res.append(subset[:])
                return
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                if sum + nums[j] > target:
                    break
                subset.append(nums[j])
                dfs(j+1, subset, sum + nums[j])
                subset.pop()
        
        dfs(0, [], 0)
        return res