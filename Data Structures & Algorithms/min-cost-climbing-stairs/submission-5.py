class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def backtrack(i, total):
            if i >= len(cost):
                return total

            key = (i, total)
            if key in memo:
                return memo[key]
            
            memo[key] = min(backtrack(i+1, total+cost[i]), backtrack(i+2, total+cost[i]))
            return memo[key]

        return min(backtrack(0, 0), backtrack(1, 0))