class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, subset, total):
            if total == target:
                res.append(subset[:])
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                subset.append(candidates[j])
                backtrack(j+1, subset, total+candidates[j])
                subset.pop()

        backtrack(0, [], 0)
        return res