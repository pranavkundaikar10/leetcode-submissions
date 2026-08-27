class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, subset, total):
            if total == target:
                res.append(subset[:])
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    continue
                if j > i and nums[j] == nums[j-1]:
                    continue
                subset.append(nums[j])
                backtrack(j, subset, total+nums[j])
                subset.pop()
                
        backtrack(0, [], 0)
        return res