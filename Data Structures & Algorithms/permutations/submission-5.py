class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subset, visited):
            if len(subset) == len(nums):
                res.append(subset[:])
            
            for j in range(0, len(nums)):
                if visited[j]:
                    continue
                visited[j] = True
                subset.append(nums[j])
                dfs(subset, visited)
                subset.pop()
                visited[j] = False


        dfs([], [False]*len(nums))
        return res

        