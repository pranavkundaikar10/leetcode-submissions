class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i, total):
            if total == amount:
                return 0
            if total > amount or i >= len(coins):
                return float('inf')
            key = (i, total)
            if key in memo:
                return memo[key]
            memo[key] = min(dfs(i+1, total), 1 + dfs(i, total + coins[i]))
            return memo[key]
        
        res = dfs(0, 0)
        return res if res != float('inf') else -1