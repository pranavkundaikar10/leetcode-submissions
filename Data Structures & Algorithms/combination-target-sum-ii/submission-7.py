class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, subset, total):
            if total == target:
                res.append(subset[:])

            for j in range(i, len(candidates)):
                if (j > i and candidates[j] == candidates[j-1]):
                    continue
                if total + candidates[j] > target:
                    break
                subset.append(candidates[j])
                backtrack(j+1, subset, total+candidates[j])
                subset.pop()
        backtrack(0, [], 0)
        return res
