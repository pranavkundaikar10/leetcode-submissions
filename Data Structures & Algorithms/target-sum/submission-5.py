class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        memo = {}
        def dfs(i, total):
            print(f'{i}, {total}')
            if i >= len(nums):
                print(f'returning {i}, {total}, {target}')
                if total == target:
                    print(f'found')
                    return 1
                return 0
            key = (i, total)
            if memo.get(key, False):
                return memo[key]
            skip = dfs(i+1, total-nums[i])
            select = dfs(i+1, total+nums[i])
            memo[key] = skip + select
            return memo[key]
        dfs(0, 0)
        return memo[(0, 0)]