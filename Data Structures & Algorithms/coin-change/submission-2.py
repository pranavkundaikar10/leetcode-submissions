class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}


        def backtrack(i, total):
            if i >= len(coins) or total > amount:
                return float("inf")
            if amount == total:
                return 0
            key = (i, total)
            if key in memo:
                return memo[key]
            
            memo[key] = min(1+backtrack(i, total+coins[i]), backtrack(i+1, total))
            return memo[key]

        res = backtrack(0, 0)
        return res if res != float('inf') else -1
