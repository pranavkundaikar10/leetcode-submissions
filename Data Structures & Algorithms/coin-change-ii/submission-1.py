class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, total):
            if total == amount:
                return 1
            if i >= len(coins) or total > amount:
                return 0

            key = (i, total)
            if key in memo:
                return memo[key]
            
            memo[key] = dfs(i, total + coins[i]) + dfs(i+1, total)
            return memo[key]

        return dfs(0, 0)