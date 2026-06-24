class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i, capacity):
            nonlocal res
            if capacity == 0:
                return 0
            if capacity < 0 or i >= len(coins):
                return float('inf')

            if (i, capacity) in memo:
                return memo[(i, capacity)]
            skip = dfs(i+1, capacity)
            select = 1 + dfs(i, capacity - coins[i])
            memo[(i, capacity)] = min(skip, select)
            return memo[(i, capacity)]
        res = dfs(0, amount)

        return res if res != float('inf') else -1