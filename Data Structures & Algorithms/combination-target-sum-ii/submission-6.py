class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, total):
            if total == target:
                res.append(subset[:])
                return
            for j in range(i , len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    continue
                subset.append(candidates[j])
                dfs(j+1, subset, total+candidates[j])
                subset.pop()


        
        dfs(0, [], 0)
        return res