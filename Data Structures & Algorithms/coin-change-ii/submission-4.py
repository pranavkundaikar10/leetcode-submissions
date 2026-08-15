class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def backtrack(i, total):
            if total == amount:
                return 1          
            if i >= len(coins) or total > amount:
                return 0

            key = (i, total)
            if key in memo:
                return memo[key]
            
            memo[key] = backtrack(i, total+coins[i]) + backtrack(i+1, total)
            return memo[key]

        return backtrack(0, 0)