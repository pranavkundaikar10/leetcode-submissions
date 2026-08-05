class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(subset, visited):
            if len(subset) == len(nums):
                res.append(subset[:])
                return res
            
            for j in range(0, len(nums)):
                if visited[j]:
                    continue
                visited[j] = True
                subset.append(nums[j])
                backtrack(subset, visited)
                subset.pop()
                visited[j] = False

        backtrack([], [False]*len(nums))

        return res