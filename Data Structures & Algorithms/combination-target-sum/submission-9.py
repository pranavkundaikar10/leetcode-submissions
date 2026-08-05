class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i , subset, total):
            if total == target:
                res.append(subset[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                if total + nums[j] > target:
                    continue

                subset.append(nums[j])
                backtrack(j, subset, total+nums[j])
                subset.pop()
        backtrack(0, [], 0)
        return res

            