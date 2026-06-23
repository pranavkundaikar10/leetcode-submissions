class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, capacity):
            if capacity == 0:
                return 1
            if capacity < 0 or i >= len(coins):
                return 0

            if (i, capacity) in memo:
                return memo[(i, capacity)]
            skip = dfs(i+1, capacity)
            select = dfs(i, capacity-coins[i])
            memo[(i, capacity)] = skip + select
            return memo[(i, capacity)]
        dfs(0, amount)
        return dfs(0, amount)