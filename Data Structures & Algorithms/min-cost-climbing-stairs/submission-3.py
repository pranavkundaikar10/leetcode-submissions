class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i, total):
            if i >= len(cost):
                return total
            key = (i, total)
            if key in memo:
                return memo[key]

            memo[key] = min(dfs(i+1, total+cost[i]), dfs(i+2, total+cost[i]))
            return memo[key]

        return min(dfs(0, 0), dfs(1,0))
