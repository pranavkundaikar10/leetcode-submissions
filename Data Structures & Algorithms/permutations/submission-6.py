class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset, visited):
            if len(subset) == len(nums):
                res.append(subset[:])

            for j in range(len(nums)):
                if visited[j]:
                    continue
                subset.append(nums[j])
                visited[j] = True
                dfs(subset, visited)
                subset.pop()
                visited[j] = False

        dfs([], [False] * len(nums))
        return res